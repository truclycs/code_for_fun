import utils
import inspect

from abstract.processor import Processor


class Stage(object):
    def __init__(self, mode=None, config_path=None, *args, **kwargs):
        if config_path is None:
            config_path = utils.Path(inspect.getfile(self.__class__)).with_name('config.yaml')

        if mode is None:
            self.processor = Processor()
        elif config_path.exists():
            config = utils.load_yaml(config_path)
            self.processor = utils.create_instance(config[mode], *args, **kwargs)
        else:
            raise FileNotFoundError('{} not found.'.format(config_path))

    def preprocess(self, *args):
        return args

    def postprocess(self, *args):
        return args

    def __call__(self, *args):
        output = self.preprocess(*args)
        output = self.processor(*output)
        output = self.postprocess(*output)
        return output
