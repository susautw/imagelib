from typing import Optional

import cv2
import numpy as np

from ...image import Image
from ...image.fillers import Filler
from ...lib import Point


class FloodFiller(Filler):
    _mask: Optional[np.ndarray]
    _point: Point

    def __init__(
            self,
            point: Optional[Point] = None,
            mask: Optional[np.ndarray] = None
    ):
        self.set_mask(mask)
        self.set_point(point)

    def set_mask(self, mask: Optional[np.ndarray]):
        self._mask = mask

    def set_point(self, point: Point):
        self._point = point if point is not None else Point(0, 0)

    def fill(self, image: 'Image', fill_value: int) -> 'Image':
        mask_size = (image.height + 2, image.width + 2)
        mask = self._mask if self._mask is not None else np.zeros(mask_size, np.uint8)

        assert mask.shape == mask_size, f'mask shape is wrong'
        filled_data = image.data.copy()
        cv2.floodFill(filled_data, mask, self._point.to_tuple(), fill_value)
        return Image(filled_data, image.color_model)
