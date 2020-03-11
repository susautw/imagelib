import threading
from math import inf
from typing import TYPE_CHECKING, Iterator

import numpy as np

from imagelib.image.image_iterator import ImageIterator

if TYPE_CHECKING:
    from imagelib.image import Image


class ThreadingImageIterator(ImageIterator, threading.Thread):
    _length: int
    _lock: threading.Lock
    _length_lock: threading.Lock
    _stored_images: np.ndarray
    _images: Iterator['Image']
    _position: int = -1

    def __init__(self, images: Iterator['Image'], length: int):
        super().__init__()
        self._lock = threading.Lock()
        self._length_lock = threading.Lock()
        self._stored_images = np.array([], dtype=object)
        self._images = images
        self._length = length
        self.setDaemon(True)
        self.start()

    def run(self) -> None:
        for image in self._images:
            with self._lock:
                self._stored_images = np.concatenate((self._stored_images, [image]))
        with self._length_lock:
            self._length = len(self._stored_images)

    @property
    def infinity(self) -> bool:
        return self._length == inf

    def __getitem__(self, item: int) -> 'Image':
        if not(self.infinity or item < len(self)):
            raise IndexError(f'image iterator out of range: {item}')
        reached = False
        while not reached:
            with self._lock:
                reached = len(self._stored_images) > item
        with self._lock:
            return self._stored_images[item]

    def __len__(self) -> int:
        with self._length_lock:
            return self._length if not self.infinity else len(self._stored_images)

    def __del__(self):
        self._stored_images = np.array([])
