import yaml

from pathlib import Path
from importlib import import_module


def load_yaml(yaml_file):
    with open(yaml_file, encoding="utf8") as f:
        configs = yaml.safe_load(f)
    return configs


def abs_path(path):
    return str(Path(__file__).parent.joinpath(path))


def eval_config(config):
    def _eval_config(config):
        if isinstance(config, dict):
            for key, value in config.items():
                if key not in ['module', 'name']:
                    config[key] = _eval_config(value)
            if 'module' in config and 'name' in config:
                module = config['module']
                class_ = config['name']
                config_kwargs = config.get(class_, {})
                return getattr(import_module(module), class_)(**config_kwargs)

            return config
        elif isinstance(config, list):
            return [_eval_config(ele) for ele in config]
        elif isinstance(config, str):
            return eval(config, {}, original_config)
        else:
            return config

    original_config = config
    config = _eval_config(config)

    if isinstance(config, dict):
        config.pop('modules', None)

    return config