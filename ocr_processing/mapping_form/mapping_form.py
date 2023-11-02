import os
import json
import random
import cv2
import argparse
from os.path import exists
from pathlib import Path


class MappingForm:
    def __init__(self):
        self.image_ext = ['jpg', 'png', 'jpeg', 'JPG', 'PNG', 'JPEG']

    def process(self, form_paths, textline_dir, output_dir):
        for form_path in form_paths:
            form_path = str(form_path)
            json_path = form_path.split('.')[0] + '.json'
            form_info, image = self.load_form_infos(json_path, form_path)
            if form_info:
                form_info, image = self.mapping(form_info, image, textline_dir)
                form_info['imagePath'] = form_info['imagePath'].split('.')[0] + '.jpg'
                self.save_new_form(form_info, image, output_dir + form_info['imagePath'].split('.')[0])

    def load_form_infos(self, json_path: str = None, image_path: str = None):
        form_info = None

        if exists(Path(json_path)):
            with open(json_path, "r") as f:
                form_info = json.load(f)

        image = cv2.imread(image_path)

        return form_info, image

    def save_new_form(self, form_info, image, output_path):
        cv2.imwrite(output_path + '.jpg', image)
        with open(output_path + '.json', "w") as f:
            json.dump(form_info, f, indent=4)

    def load_text_lines(self, text_line_path: str = None):
        text = ""
        image = cv2.imread(text_line_path)

        if exists(text_line_path.split('.')[0] + '.txt'):
            with open(text_line_path.split('.')[0] + '.txt', "r") as f:
                text = f.read()
        return image, text

    # def get_images(self, directory="."):
    #     all_images = []
    #     for img in os.listdir(directory):
    #         ext = img.split(".")[len(img.split(".")) - 1]
    #         if (ext in self.image_ext):
    #             all_images.append(img)
    #     return all_images

    def mapping(self, form_info, image, textline_dir):
        boxes = form_info['shapes']
        for i, box in enumerate(boxes):
            point = box['points']
            label = box['label']

            if len(point) == 2:
                if (point[0][0] > point[1][0]):
                    point[0], point[1] = point[1], point[0]
                box_image = image[int(point[0][1]):int(point[1][1]), int(point[0][0]):int(point[1][0])]
            else:
                continue

            text_line_path = Path(textline_dir).joinpath(label)

            if exists(text_line_path):
                file_path = 'zzz.txt'
                while file_path.split('.')[-1] == 'txt':
                    file_path = str(text_line_path) + '/' + random.choice(os.listdir(text_line_path))
                text_line_image, value = self.load_text_lines(file_path)
                boxes[i]['value'] = value

                merge_text_line = self.merge(box_image, text_line_image)
                image[int(point[0][1]):int(point[1][1]), int(point[0][0]):int(point[1][0]), :] = merge_text_line

        form_info['shapes'] = boxes
        form_info['imageData'] = None
        return form_info, image

    def merge(self, box, text_line):
        text_line = cv2.resize(text_line, (box.shape[1], box.shape[0]))
        merge_image = cv2.bitwise_and(text_line, box)
        return merge_image


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--form-dir', help='path to file')
    parser.add_argument('--textline-dir', help='path to file')
    parser.add_argument('--output-dir', default='output/')
    parser.add_argument('--patterns', nargs="+", default=['*.jpg', '*.png', '*.jpeg', '*.JPG', '*.PNG', '*.JPEG'])
    args = parser.parse_args()

    output_dir = args.output_dir if args.output_dir else None
    textline_dir = Path(args.textline_dir)

    patterns = args.patterns
    form_dir = Path(args.form_dir)
    form_paths = []
    for pattern in patterns:
        form_paths += list(form_dir.glob(f'**/{pattern}'))

    mapping_form = MappingForm()
    mapping_form.process(form_paths, textline_dir, output_dir)
