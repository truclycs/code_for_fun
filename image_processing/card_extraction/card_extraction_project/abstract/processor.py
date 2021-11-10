class Processor(object):
    def preprocess(self, *args):
        return args

    def process(self, *args):
        return args

    def postprocess(self, *args):
        return args

    def __call__(self, *args):
        output = self.preprocess(*args)
        output = self.process(*output)
        output = self.postprocess(*output)
        return output
