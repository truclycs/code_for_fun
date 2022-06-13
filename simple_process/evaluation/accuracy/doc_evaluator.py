import os
import sys
import json
from pathlib import Path
from shapely.geometry import Polygon

import accuracy.utils as utils

sys.path.append(os.environ['PWD'])


class DocEvaluator:
    def __init__(self, doc_reporter, report_name, ignored_fields, iou_threshold):
        self.report_name = report_name
        self.iou_threshold = iou_threshold
        self.ignored_fields = ignored_fields
        self.doc_reporter = doc_reporter

        report_dir = Path(utils.abs_path(doc_reporter.output_dir))
        if not report_dir.exists():
            report_dir.mkdir(parents=True)

    def mapping_info(self, label_json, pred_json):
        file_name = label_json['imagePath']

        if file_name[0] == '=':
            file_name = "'" + file_name  # help for exporting xlsx file.

        mapping_infos = []
        compared_fields = []
        for label_shape in label_json['shapes']:
            field_name = label_shape['label'].upper()

            if field_name not in compared_fields and field_name not in self.ignored_fields:
                mapping_info = {'file_name': file_name,
                                'field_name': field_name,
                                'label': label_shape.get('value', ''),
                                'ocr': '',
                                'type': 'text'}

                # get labeled text box
                if label_shape['shape_type'] == 'polygon':
                    label_box = label_shape['points']
                elif label_shape['shape_type'] == 'rectangle':
                    label_box = self._to_4points(label_shape['points'])
                else:
                    continue
                    # raise RuntimeError('Found a line in label shapes.')

                max_inter_area = 0.
                # ensure get a predicted box which have maximum intersection area with labeled box
                for pred_shape in pred_json['shapes']:
                    if field_name == pred_shape['label']:
                        # get predicted text box
                        if pred_shape['shape_type'] == 'polygon':
                            pred_box = pred_shape['points']
                        elif pred_shape['shape_type'] == 'rectangle':
                            pred_box = self._to_4points(pred_shape['points'])
                        else:
                            continue
                            # raise RuntimeError('Found a line in label shapes.')

                        iou, inter_area = self._compute_iou(pred_box, label_box)
                        # get ocr value of predicted box which have reasonable iou and itersection area with labeled box
                        if (iou >= self.iou_threshold) and (inter_area >= max_inter_area):
                            mapping_info['ocr'] = pred_shape.get('value', '')
                            max_inter_area = inter_area
                            compared_fields.append(field_name)

                mapping_infos.append(mapping_info)

        return mapping_infos

    def _to_4points(self, points):
        x1, y1 = points[0][0], points[0][1]
        x2, y2 = points[1][0], points[1][1]
        return [(x1, y1), (x2, y1), (x2, y2), (x1, y2)]

    def _compute_iou(self, box1, box2):
        box1, box2 = Polygon(box1), Polygon(box2)
        inter_area = box1.intersection(box2).area
        union_area = box1.union(box2).area
        iou = inter_area / union_area
        return iou, inter_area

    def _load_json(self, path):
        with open(str(path), mode='r', encoding='utf-8') as f:
            return json.load(f)

    def __call__(self, label_paths, pred_paths):
        mapping_infos = []
        for label_path, pred_path in zip(label_paths, pred_paths):
            assert Path(label_path).name == Path(pred_path).name, 'label and pred file must be same name.'
            label_json = self._load_json(label_path)
            pred_json = self._load_json(pred_path)
            mapping_infos.extend(self.mapping_info(label_json, pred_json))

        # export xlsx file
        self.doc_reporter.is_verification = True
        self.doc_reporter.save(data=mapping_infos, file_name=self.report_name)
