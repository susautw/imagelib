from abc import abstractmethod, ABC
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from imagelib.image import Image


class ImageIterator(ABC):

    @property
    @abstractmethod
    def infinity(self) -> bool:
        pass

    @abstractmethod
    def __getitem__(self, item: int) -> 'Image':
        pass

    @abstractmethod
    def __len__(self) -> int:
        pass
