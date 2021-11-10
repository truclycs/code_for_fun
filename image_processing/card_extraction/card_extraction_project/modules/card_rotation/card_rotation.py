from abstract.stage import Stage


class CardRotation(Stage):
    def __init__(self, mode):
        super(CardRotation, self).__init__(mode)

    def preprocess(self, card_infos):
        if __debug__:
            for i, card_info in enumerate(card_infos):
                assert type(card_info.image).__name__ == 'ndarray', f'Image #{i} must be an ndarray.'
                assert card_info.image.ndim == 3, f'Image #{i} must be a 3D ndarray.'
                assert card_info.image.shape[-1] == 3, f'Image #{i} must have 3 channels.'

        return card_infos,

    def postprocess(self, card_infos, rotated_images, rotated_angles, scores):
        for card_info, rotated_image, rotated_angle, score in zip(card_infos, rotated_images, rotated_angles, scores):
            card_info.image = rotated_image
            card_info.angle = rotated_angle
            card_info.card_confidence.rotation = score

        return card_infos,