from typing import TYPE_CHECKING, Iterator

from imagelib.image.image_iterator import ImageIterator

if TYPE_CHECKING:
    from imagelib.image import Image


class NonStoreImageIterator(ImageIterator):
    _images: Iterator['Image']
    _length: int

    def __init__(self, images: Iterator['Image'], length: int):
        self._images = images
        self._length = length

    @property
    def infinity(self) -> bool:
        return False

    def __getitem__(self, item: int) -> 'Image':
        return next(self._images)

    def __len__(self) -> int:
        return self._length
