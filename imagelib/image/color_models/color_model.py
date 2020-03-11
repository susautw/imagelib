from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from imagelib.patterns import Singleton

if TYPE_CHECKING:
    from imagelib.image import Image


class ColorModel(ABC, Singleton):

    @abstractmethod
    def number_of_channels(self) -> int:
        pass

    @abstractmethod
    def to_rgb(self, context: 'Image') -> 'Image':
        pass

    @abstractmethod
    def to_hsv(self, context: 'Image') -> 'Image':
        pass

    @abstractmethod
    def to_bgr(self, context: 'Image') -> 'Image':
        pass

    @abstractmethod
    def to_gray(self, context: 'Image') -> 'Image':
        pass
