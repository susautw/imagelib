from pathlib import Path
from typing import TYPE_CHECKING

import cv2

from ...image.image_writers import ImageWriter
from ...patterns import Singleton

if TYPE_CHECKING:
    from ...image import Image


class BlockingImageWriter(ImageWriter, Singleton):
    def write(self, image: 'Image', path: Path):
        cv2.imwrite(str(path), image.to_numpy())
