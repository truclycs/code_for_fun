import cv2
import random
import numpy as np
import imgaug.augmenters as iaa

from pathlib import Path
from base_copy_paste import BaseCopyPaste

__all__ = ['SimpleCopyPaste']


class SimpleCopyPaste(BaseCopyPaste):
    def __init__(
        self,
        background_dir,  # directory where storages all back ground images.
        template_ratio,  # ratio between template and background.
        template_type=None,  # name of template. Ex: CARD_BACK, CMND_BACK, ...
        image_pattern='*.*',  # pattern of all background images.
        bg_required_transforms=None,  # augmentations used for background.
        bg_optional_transforms=None,  # augmentations used for background.
        fg_required_transforms=None,  # augmentations used for template (foreground).
        fg_optional_transforms=None,  # augmentations used for template (foreground).
        output_required_transforms=None,  # do not use augmentations about geometric, size.
        output_optional_transforms=None,  # do not use augmentations about geometric, size.
        *args, **kwargs,
    ):
        super(SimpleCopyPaste, self).__init__(*args, **kwargs)
        self.template_type = template_type
        self.template_ratio = template_ratio
        self.fg_optional_transforms = fg_optional_transforms if fg_optional_transforms is not None else []
        self.fg_required_transforms = fg_required_transforms if fg_required_transforms is not None else []
        self.bg_optional_transforms = bg_optional_transforms if bg_optional_transforms is not None else []
        self.bg_required_transforms = bg_required_transforms if bg_required_transforms is not None else []
        self.output_optional_transforms = output_optional_transforms if output_optional_transforms is not None else []
        self.output_required_transforms = output_required_transforms if output_required_transforms is not None else []

        self.bg_images = list(Path(background_dir).glob(image_pattern))

    def apply(self, image, label):
        '''
        Args:
            image: template image
            label: json path or json label of template
        Outputs:
            image: combinated image between template and random background
            label: json label of template on random background
        '''

        image, label, mask, points = self.get_template_info(image, label, self.template_type)

        # choose back ground image randomly
        bg_image = cv2.imread(str(random.choice(self.bg_images)))

        # required augmentations for background
        for augmenter in random.sample(
            self.bg_required_transforms,
            k=len(self.bg_required_transforms)
        ):
            bg_image = augmenter(image=bg_image)

        # optional augmentions for background
        for augmenter in random.sample(
            self.bg_optional_transforms,
            k=random.randint(0, len(self.bg_optional_transforms))
        ):
            bg_image = augmenter(image=bg_image)

        # required augmentations for foreground image, mask, labeled points of teample
        for augmenter in random.sample(
            self.fg_required_transforms,
            k=len(self.fg_required_transforms)
        ):
            image, mask, points = augmenter(
                image=image,
                segmentation_maps=mask,
                keypoints=points,
            )

        # optional augmentations for foreground image, mask, labeled points of teample
        for augmenter in random.sample(
            self.fg_optional_transforms,
            k=random.randint(0, len(self.fg_optional_transforms))
        ):
            image, mask, points = augmenter(
                image=image,
                segmentation_maps=mask,
                keypoints=points,
            )

        # set ratio between fore ground and back ground
        height, width = image.shape[:2]
        bg_height, bg_width = bg_image.shape[:2]

        if max(height, width) > min(bg_height, bg_width) * self.template_ratio:
            if height >= width:
                h = min(bg_height, bg_width) * max(self.template_ratio, 0.7)
                w = h * width / height
            else:
                w = min(bg_height, bg_width) * max(self.template_ratio, 0.7)
                h = w * height / width

            # resize to appropriate size between foreground and background
            resize_to_size = iaa.Resize({"height": int(round(h)), "width": int(round(w))})
            image, mask, points = resize_to_size(
                image=image,
                segmentation_maps=mask,
                keypoints=points
            )
        else:
            w, h = width / self.template_ratio, height / self.template_ratio
            bg_image = iaa.CropToFixedSize(
                width=int(round(w)),
                height=int(round(h))
            )(image=bg_image)

        # pad foreground image, mask, labeled points to fix with background size
        pad_to_size = iaa.PadToFixedSize(
            width=bg_image.shape[1],
            height=bg_image.shape[0]
        )
        image, mask, points = pad_to_size(
            image=image,
            segmentation_maps=mask,
            keypoints=points
        )

        # set all transformed points to new label (json info)
        points = [[float(point.x), float(point.y)] for point in points.keypoints]
        label = self.set_points(label, points)
        label['imageHeight'], label['imageWidth'] = image.shape[0], image.shape[1]

        # blend fore ground mask with gaussian blur
        mask = mask.get_arr().astype(np.float32)
        k = max(max(image.shape) // 300 * 2 + 1, 5)
        mask = cv2.GaussianBlur(mask, ksize=(k, k), sigmaX=k)

        # combinate fore ground and back ground with fore ground mask
        image = image * mask + bg_image * (1. - mask)
        image = image.astype(np.uint8)

        # required augmentaions for combinated image,
        # just uses augmentations about color, blur, blend, contrast, ...
        # do not use augmentations about gemetric, size.
        for augmenter in random.sample(
            self.output_optional_transforms,
            k=random.randint(0, len(self.output_optional_transforms))
        ):
            image = augmenter(image=image)

        # optional augmentaions for combinated image,
        # just uses augmentations about color, blur, blend, contrast, ...
        # do not use augmentations about gemetric, size.
        for augmenter in random.sample(
            self.output_optional_transforms,
            k=random.randint(0, len(self.output_optional_transforms))
        ):
            image = augmenter(image=image)

        return image, label
