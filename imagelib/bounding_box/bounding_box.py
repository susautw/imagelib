from abc import ABC, abstractmethod

from ..image import Image
from ..lib import Brush


class BoundingBox(ABC):
    @abstractmethod
    def draw_to_image(
            self,
            image: Image,
            brush: Brush
    ):
        pass

    @abstractmethod
    def crop_image(self, image: Image):
        pass
