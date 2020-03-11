from pathlib import Path
from typing import TYPE_CHECKING

import cv2
import numpy as np
from imagelib.image.image_writers import BlockingImageWriter
from ..lib import Point

if TYPE_CHECKING:
    from imagelib.image import NamedWindow
    from imagelib.image.color_models import ColorModel
    from imagelib.image.image_writers import ImageWriter


class Image:
    _data: np.ndarray
    _color_model: 'ColorModel'

    def __init__(self, data: np.ndarray, color_model: 'ColorModel'):
        self._data = data
        self._color_model = color_model

    @property
    def data(self) -> np.ndarray:
        return self._data

    @property
    def color_model(self):
        return self._color_model

    @property
    def height(self):
        return self.data.shape[0]

    @property
    def width(self):
        return self.data.shape[1]

    @property
    def center_point(self):
        return Point(self.width // 2, self.height // 2)

    def to_numpy(self) -> np.ndarray:
        return self.data

    def show(self, window: 'NamedWindow') -> None:
        cv2.imshow(window.name, self.to_numpy())

    def save(self, path: Path, writer: 'ImageWriter' = BlockingImageWriter()):
        writer.write(self, path)

    def clone(self) -> 'Image':
        return Image(self.data.copy(), self.color_model)

    def number_of_channels(self) -> int:
        return self.color_model.number_of_channels()

    def to_rgb(self) -> 'Image':
        return self.color_model.to_rgb(self)

    def to_bgr(self) -> 'Image':
        return self.color_model.to_bgr(self)

    def to_hsv(self) -> 'Image':
        return self.color_model.to_hsv(self)

    def to_gray(self) -> 'Image':
        return self.color_model.to_gray(self)

    def __invert__(self):
        return Image(cv2.bitwise_not(self.to_numpy()), self.color_model)

    def __and__(self, other: 'Image'):
        return Image(cv2.bitwise_and(self.to_numpy(), other.to_numpy()), self.color_model)

    def __or__(self, other: 'Image'):
        return Image(cv2.bitwise_or(self.to_numpy(), other.to_numpy()), self.color_model)

    def __xor__(self, other: 'Image'):
        return Image(cv2.bitwise_xor(self.to_numpy(), other.to_numpy()), self.color_model)

    def __del__(self):
        self._data = np.array([])
