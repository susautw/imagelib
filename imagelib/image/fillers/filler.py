from abc import ABC, abstractmethod
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from imagelib.image import Image


class Filler(ABC):

    @abstractmethod
    def fill(self, image: 'Image', fill_value: int) -> 'Image':
        pass
