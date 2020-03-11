from typing import List, TYPE_CHECKING

from imagelib.image.image_iterator import ImageIterator

if TYPE_CHECKING:
    from imagelib.image import Image


class ListImageIterator(ImageIterator):
    images: List['Image']

    def __init__(self, images: List['Image']):
        self.images = images

    @property
    def infinity(self) -> bool:
        return False

    def __getitem__(self, item: int) -> 'Image':
        return self.images[item]

    def __len__(self) -> int:
        return len(self.images)
