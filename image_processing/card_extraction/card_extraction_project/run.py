import cv2
import time
import utils
import argparse
import numpy as np
from pathlib import Path
from natsort import natsorted


def module_time(module, module_name, *args):
    start = time.time()
    output = module(*args)
    stop = time.time()
    print('{}: {:.4f}s'.format(module_name, stop - start))
    return output


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input_dir', help='path to image.')
    parser.add_argument('--output-dir', help='path to save image')
    parser.add_argument('--pattern', help='glob pattern if image_path is a dir.')
    parser.add_argument('--starting-file', default=1)
    args = parser.parse_args()

    if args.pattern:
        image_paths = natsorted(Path(args.input_dir).glob(args.pattern), key=lambda x: x.stem)
    else:
        image_paths = [Path(args.input_dir)]

    output_dir = Path(args.output_dir) if args.output_dir else Path('output')
    if not output_dir.exists():
        output_dir.mkdir(parents=True)

    config = utils.load_yaml('config.yaml')
    card_extractor = utils.create_instance(config['card_extraction'])
    print('[INFO] mode: ', config['card_extraction']['CardExtraction']['mode'], '\n')

    if not output_dir.exists():
        output_dir.mkdir(parents=True)

    for idx, image_path in enumerate(image_paths[int(args.starting_file) - 1:], int(args.starting_file)):
        print(f'[{idx} / {len(image_paths)}] image name: {image_path.name}')
        card_infos, = module_time(card_extractor, 'Card Extraction', cv2.imread(str(image_path)))

        if not len(card_infos):
            print(image_path.name)

        for i, card_info in enumerate(card_infos):
            box = np.int32([[point.x, point.y] for point in card_info.location])
            card_info.original_image = cv2.polylines(card_info.original_image, [box], True, color=[0, 255, 0], thickness=3)

            cv2.putText(card_info.original_image,
                        text=f'card - {card_info.card_confidence.card_extraction}',
                        org=tuple(box[0]),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=0.001 * max(card_info.image.shape[0], card_info.image.shape[1]),
                        color=[0, 255, 0],
                        thickness=3, lineType=cv2.LINE_AA)
            # save card
            card_info.image = np.ascontiguousarray(card_info.image, dtype=np.uint8)
            image_name = image_path.name if i == 0 else f'{image_path.stem}_{i}{image_path.suffix}'
            cv2.imwrite(str(output_dir.joinpath(image_name)), card_info.image)

        # save card
        cv2.imwrite(str(output_dir.joinpath(f'{image_path.name}_card{image_path.suffix}')), card_info.original_image)
