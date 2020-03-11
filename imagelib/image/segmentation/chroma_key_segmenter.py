from typing import List

import cv2
import numpy as np

from imagelib.image import Image
from ..color_models import GrayColor
from ..segmentation.image_segmenter import ImageSegmenter


class ChromaKeySegmenter(ImageSegmenter):
    _mask_lower: np.ndarray
    _mask_higher: np.ndarray

    def set_mask(self, lower: np.ndarray, higher: np.ndarray):
        self._mask_lower = lower
        self._mask_higher = higher

    def set_background(self, background_image: Image, z_value: float):
        background_hsv = background_image.to_hsv()
        background_flattened = self._flatten_background(background_hsv.to_numpy())

        low = []
        high = []

        for i in range(3):
            mu = background_flattened[i].mean()
            sigma = background_flattened[i].std()
            deviation = z_value * sigma
            low.append(self._restrict(mu - deviation))
            high.append(self._restrict(mu + deviation))

        self._mask_lower = np.array([low[0], low[1], low[2]])
        self._mask_higher = np.array([high[0], high[1], high[2]])

    @staticmethod
    def _flatten_background(background: np.ndarray) -> List[np.ndarray]:
        flattened = []
        for i in range(3):
            background_series = background.flatten()
            flattened.append(background_series)
        return flattened

    @staticmethod
    def _restrict(color_component):
        return np.clip(color_component, 0, 255)

    def segment(self, image: Image) -> Image:
        image_hsv = image.to_hsv()
        image_mask = cv2.inRange(image_hsv.to_numpy(), self._mask_lower, self._mask_higher)
        image_mask = cv2.bitwise_not(image_mask)

        return Image(image_mask, GrayColor())
