from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
from pathlib import Path

if TYPE_CHECKING:
    from imagelib.image import Image


class ImageWriter(ABC):

    @abstractmethod
    def write(self, image: 'Image', path: Path):
        pass
