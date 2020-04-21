from abc import ABC, abstractmethod

from . import Brush, BrushFactory
from ..image import Image


class Drawable(ABC):

    @abstractmethod
    def draw(self, image: Image, brush: Brush = BrushFactory().get_default_brush()) -> Image:
        pass
