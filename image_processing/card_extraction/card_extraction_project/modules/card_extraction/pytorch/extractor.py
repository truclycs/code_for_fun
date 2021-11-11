import cv2
import utils
import torch
import torchvision

from shapely import geometry
from abstract.processor import Processor


class CardExtractor(Processor):
    def __init__(self, arch_config, warper_config, pred_score_threshold, nms_iou_threshold, card_area_threshold, weight_path, image_size, cuda):
        super(CardExtractor, self).__init__()
        self.image_size = image_size
        self.nms_iou_threshold = nms_iou_threshold
        self.card_area_threshold = card_area_threshold
        self.pred_score_threshold = pred_score_threshold
        self.device = torch.device('cuda' if cuda else 'cpu')
        self.card_warper = utils.create_instance(warper_config)
        self.model = utils.create_instance(arch_config)
        self.model.load_state_dict(torch.load(utils.abs_path(weight_path), map_location='cpu'))
        self.model.to(self.device)
        self.model.eval()

    def preprocess(self, image):
        sample = cv2.resize(image, dsize=self.image_size)
        sample = torch.from_numpy(sample).to(self.device).to(torch.float)
        samples = sample.unsqueeze(dim=0).permute(0, 3, 1, 2)
        samples = (samples - samples.mean()) / samples.std()
        return samples, image

    def process(self, samples, image):
        with torch.no_grad():
            return self.model(samples), image

    def postprocess(self, preds, image):
        pred = preds[0]

        boxes, scores, masks = pred['boxes'], pred['scores'], pred['masks']

        indices = scores > self.pred_score_threshold
        boxes, scores, masks = boxes[indices], scores[indices], masks[indices]

        indices = torchvision.ops.nms(boxes, scores, self.nms_iou_threshold)
        masks = masks[indices]
        masks = masks.squeeze(1).detach().cpu().numpy()

        _warped_cards, _warped_scores, _warped_locations = [], [], []
        for mask in masks:
            cards, locations, scores = self.card_warper(image, mask)
            _warped_cards.extend(cards)
            _warped_scores.extend(scores)
            _warped_locations.extend(locations)

        max_card_area = max([geometry.Polygon(location).area for location in _warped_locations]) if len(_warped_locations) else 0

        warped_cards, warped_scores, warped_locations = [], [], []
        for card, score, location in zip(_warped_cards, _warped_scores, _warped_locations):
            if geometry.Polygon(location).area > self.card_area_threshold * max_card_area:
                warped_cards.append(card)
                warped_scores.append(score)
                warped_locations.append(location)

        return image, warped_cards, warped_scores, warped_locations
