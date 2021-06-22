# Tao service credential file tren Google Console va download file key json
# pip install google-cloud-vision
# export GOOGLE_APPLICATION_CREDENTIALS=keyfile.json
# python google_vision_api.py input_dir output_dir


import json
from google.cloud import vision
from google.cloud.vision_v1.types.image_annotator import AnnotateImageRequest, AnnotateImageResponse
from google.protobuf import json_format
import io
from pathlib import Path
from argparse import ArgumentParser
import time


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('input_dir', type=Path)
    parser.add_argument('output_dir', type=Path)
    parser.add_argument('--ext', default='png')
    args = parser.parse_args()

    client = vision.ImageAnnotatorClient()
    image_paths = sorted(list(args.input_dir.glob(f'*.{args.ext}')))
    for i, image_path in enumerate(image_paths, 1):

        with io.open(image_path, 'rb') as image_file:
            content = image_file.read()

        image = vision.Image(content=content)
        request = AnnotateImageRequest(image=image, image_context=vision.ImageContext(language_hints='vi'))
        response: AnnotateImageResponse = client.annotate_image(request=request)
        #  = client.document_text_detection(image=image)

        if response.error.message:
            print(image_path, response.error.message)
            continue

        text = response.full_text_annotation.text
        output_path = args.output_dir.joinpath(image_path.with_suffix('.txt').name)
        output_path.parent.mkdir(exist_ok=True, parents=True)
        with open(output_path, 'wt', encoding='utf-8') as f:
            f.write(text)

        print(f'[Done] [{i}/{len(image_paths)}] {output_path}')

