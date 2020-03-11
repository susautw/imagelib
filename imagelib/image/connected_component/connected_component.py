from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from imagelib.image import Image


class ConnectedComponent(ABC):
    @abstractmethod
    def compute(self, image: 'Image') -> 'Image':
        pass
