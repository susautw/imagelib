from abc import ABC, abstractmethod

from imagelib.image import Image


class ImageSegmenter(ABC):

    @abstractmethod
    def segment(self, image: Image) -> Image:
        pass
