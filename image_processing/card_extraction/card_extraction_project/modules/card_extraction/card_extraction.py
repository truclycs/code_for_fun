from abstract.stage import Stage
from ..transfer_object import Point, CardInfo, CardConfidence, SanityConfidence


class CardExtraction(Stage):
    def __init__(self, mode):
        super(CardExtraction, self).__init__(mode)

    def preprocess(self, image):
        if __debug__:
            assert type(image).__name__ == 'ndarray', 'image must be ndarray.'
            assert len(image.shape) == 3, 'image must be a 3D ndarray.'
            assert image.shape[-1] == 3, 'image must have 3 channels.'
        return image,

    def postprocess(self, image, warped_cards, warped_confidences, warped_locations):
        card_infos = []
        for idx, (warped_card, warped_location, warped_confidence) in enumerate(zip(warped_cards, warped_locations, warped_confidences)):
            card_info = CardInfo()
            card_confidence = CardConfidence(card_extraction=warped_confidence)
            sanity_confidence = SanityConfidence()
            card_info.idx = idx
            card_info.image = warped_card
            card_info.original_image = image
            card_info.card_confidence = card_confidence
            card_info.sanity_confidence = sanity_confidence
            card_info.warped_size = warped_card.shape[1::-1]
            card_info.location = [Point(int(point[0]), int(point[1])) for point in warped_location]
            card_infos.append(card_info)

        return card_infos,
