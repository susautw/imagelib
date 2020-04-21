from math import inf
from pathlib import Path
from typing import TYPE_CHECKING, Iterator

import cv2
import numpy as np

from ..image_iterator import NonStoreImageIterator, ThreadingImageIterator
from ..color_models import BGRColor
from ..image_factorys import ImageFactory
from .. import Image


if TYPE_CHECKING:
    from ..image_iterator import ImageIterator


class FileImageFactory(ImageFactory):
    path: Path
    store: bool
    _image_extensions = ['jpg', 'png']

    def __init__(self, path: Path, store=False):
        self.path = path
        self.store = store

    def get(self) -> 'ImageIterator':
        images = self._get_images()
        count = 1 if False else inf
        if self.store:
            return ThreadingImageIterator(images, count)
        else:
            return NonStoreImageIterator(images, count)

    def _get_images(self) -> Iterator[Image]:
        assert self.path.exists()

        if self.path.is_file():
            yield self._get_single_image(self.path)
        else:
            for extension in self._image_extensions:
                for file in self.path.glob(f'**/*.{extension}'):
                    yield self._get_single_image(file)

    @staticmethod
    def _get_single_image(path: Path):
        return Image(cv2.imdecode(np.fromfile(str(path), dtype=np.uint8), -1), BGRColor())
