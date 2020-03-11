from abc import ABC, abstractmethod
from imagelib.image.image_iterator import ImageIterator


class ImageFactory(ABC):

    @abstractmethod
    def get(self) -> ImageIterator:
        pass
