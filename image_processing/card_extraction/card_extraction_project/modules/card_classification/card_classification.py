from abstract.stage import Stage


class CardClassification(Stage):
    def __init__(self, mode):
        super(CardClassification, self).__init__(mode)

    def preprocess(self, card_infos):
        if __debug__:
            for i, card_info in enumerate(card_infos):
                assert type(card_info.image).__name__ == 'ndarray', f'Image #{i} must be an ndarray.'
                assert card_info.image.ndim == 3, f'Image #{i} must be a 3D ndarray.'
                assert card_info.image.shape[-1] == 3, f'Image #{i} must have 3 channels.'

        return card_infos,

    def postprocess(self, card_infos, card_types, scores):
        for card_info, card_type, score in zip(card_infos, card_types, scores):
            card_info.card_type = card_type
            card_info.card_confidence.classification = score
        return card_infos,