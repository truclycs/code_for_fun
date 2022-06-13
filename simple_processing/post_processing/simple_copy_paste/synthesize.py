import cv2
import yaml
import json
import random
import argparse

from pathlib import Path
from importlib import import_module


def load_yaml(yaml_file):
    with open(yaml_file) as f:
        settings = yaml.safe_load(f)
    return settings


def create_instance(config, *args, **kwargs):
    module = config['module']
    name = config['name']
    config_kwargs = config.get(name, {})
    for key, value in config_kwargs.items():
        if isinstance(value, str):
            config_kwargs[key] = eval(value)
        elif isinstance(value, list):
            config_kwargs[key] = [eval(v) for v in value]
    return getattr(import_module(module), name)(*args, **config_kwargs, **kwargs)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, default='config.yaml')
    parser.add_argument('--input-dir', type=str, default='./sample/foreground/')
    parser.add_argument('--output-dir', type=str, default='./sample/synthesize/')
    parser.add_argument('--repeat', type=int, default=1)
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    if not output_dir.exists():
        output_dir.mkdir(parents=True)

    config = load_yaml(args.config)
    copy_paste = create_instance(config)

    label_paths = list(Path(args.input_dir).glob('**/*.json'))

    for i in range(args.repeat):
        for label_path in label_paths:
            print('*' * 30)
            print(str(label_path))

            with label_path.open(mode='r', encoding='utf-8') as f:
                label = json.load(f)

            image_name = Path(label['imagePath']).name
            image = cv2.imread(str(label_path.with_name(image_name)))

            image, label = copy_paste(image, label)

            idx = random.randint(1, 1000)
            image_path = output_dir.joinpath(f'{label_path.stem}_{idx}{Path(image_name).suffix}')
            json_path = output_dir.joinpath(f'{label_path.stem}_{idx}.json')

            label['imagePath'] = image_path.name
            with json_path.open(mode='w', encoding='utf-8') as f:
                json.dump(label, f, indent=4, ensure_ascii=False)

            cv2.imwrite(str(image_path), image)
