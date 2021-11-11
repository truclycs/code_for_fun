import cv2
import numpy as np
import torch

import utils
from abstract.processor import Processor 
from torchvision.models import MobileNetV2


class CardClassifier(Processor):
    def __init__(self, classes, num_classes, weight_path, image_size, cuda, bin_threshold):
        self.classes = classes
        self.image_size = image_size
        self.bin_threshold = bin_threshold

        self.device = torch.device('cuda' if cuda else 'cpu')
        self.model = MobileNetV2(num_classes)
        self.model.load_state_dict(torch.load(utils.abs_path(weight_path), map_location='cpu'))
        self.model.to(self.device)
        self.model.eval()

    def preprocess(self, card_infos):
        images = [card_info.image for card_info in card_infos]
        samples = [cv2.resize(image, self.image_size) for image in images]
        samples = np.array(samples)
        samples = torch.from_numpy(samples).to(self.device).to(torch.float)
        samples = samples.permute(0, 3, 1, 2)
        samples = (samples - samples.mean()) / samples.std()
        return card_infos, samples

    def process(self, card_infos, samples):
        with torch.no_grad():
            preds = self.model(samples).softmax(dim=1)
        return card_infos, preds

    def postprocess(self, card_infos, preds):
        card_types = [self.classes[pred.argmax().item()] for pred in preds]
        scores = [pred[pred.argmax()].item() for pred in preds]
        card_types = [card_types if score > self.bin_threshold else 'others' for card_type, score in zip(card_types, scores)]
        return card_infos, card_types, scores