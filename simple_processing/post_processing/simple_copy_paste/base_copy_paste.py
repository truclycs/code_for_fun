import cv2
import json
import numpy as np
from abc import ABC, abstractmethod
from imgaug.augmentables import Keypoint
from imgaug.augmentables import KeypointsOnImage
from imgaug.augmentables.segmaps import SegmentationMapsOnImage


class BaseCopyPaste(ABC):
    def __call__(self, image, label):
        image, label = self.apply(image, label)
        return image, label

    @abstractmethod
    def apply(self, image, label):
        pass

    def get_template_info(self, image, label, template_type=None):
        # get fore ground points from label
        points, label = self.get_points(label)
        points = [Keypoint(x=point[0], y=point[1]) for point in points]
        points = KeypointsOnImage(keypoints=points, shape=image.shape)

        # get fore ground mask from getting region from label
        mask = self.get_template_mask(label, template_type) if template_type else np.ones_like(image)
        mask = SegmentationMapsOnImage(arr=mask, shape=image.shape)

        return image, label, mask, points

    def get_template_mask(self, label, template_type):
        height, width = label['imageHeight'], label['imageWidth']
        mask = np.zeros(shape=(height, width, 3), dtype=np.uint8)
        is_created = False

        for shape in label['shapes']:
            if shape['label'] == template_type:
                if shape['shape_type'] == 'rectangle':
                    points = self.to_4points(shape['points'])
                elif shape['shape_type'] == 'polygon':
                    points = shape['points']
                else:
                    raise ValueError('type of label region must be rectangle or polygon.')

                cv2.fillPoly(img=mask, pts=[np.int32(points)], color=(1, 1, 1))

                is_created = True

        if not is_created:
            raise TypeError(f'label must be contained template label {template_type}.')

        return mask

    def get_points(self, label):
        if isinstance(label, str):
            with open(file=label, mode='r', encoding='utf-8') as f:
                label = json.load(f)
            points = get_points(label)
        elif isinstance(label, dict):
            points = get_points(label)
        else:
            raise TypeError('label must be str, dict.')
        return points, label

    def set_points(self, label, points):
        label = set_points(label, points)
        return label

    def to_4points(self, points):
        x1, y1 = points[0][0], points[0][1]
        x2, y2 = points[1][0], points[1][1]
        return [(x1, y1), (x2, y1), (x2, y2), (x1, y2)]


def get_points(json_info):
    points = []
    if isinstance(json_info, dict):
        for key, value in json_info.items():
            if key == 'points':
                points += value
            else:
                points += get_points(value)
    elif isinstance(json_info, list):
        for element in json_info:
            points += get_points(element)

    return points


def set_points(json_info, points):
    if isinstance(json_info, dict):
        for key, value in json_info.items():
            if key == 'points':
                for i in range(len(value)):
                    value[i] = points.pop(0)
            else:
                set_points(value, points)

    elif isinstance(json_info, list):
        for element in json_info:
            set_points(element, points)

    return json_info
