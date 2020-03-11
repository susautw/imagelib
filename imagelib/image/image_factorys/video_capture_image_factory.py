from math import inf
from typing import Iterator

import cv2

import imagelib.image.color_models
from ...image.image_factorys import ImageFactory
from ...image import Image
from ...image.image_iterator import ImageIterator, ThreadingImageIterator, NonStoreImageIterator


class VideoCaptureImageFactory(ImageFactory):
    capture: cv2.VideoCapture
    store: bool

    def __init__(self, capture: cv2.VideoCapture, store: bool = False):
        self.set_capture(capture)
        self.store = store

    def set_capture(self, capture: cv2.VideoCapture):
        self.capture = capture

    def get(self) -> ImageIterator:
        count = int(self.capture.get(cv2.CAP_PROP_FRAME_COUNT))
        count = count if count != -1 else inf
        if self.store:
            return ThreadingImageIterator(self._get_images(), count)
        else:
            return NonStoreImageIterator(self._get_images(), count)

    def _get_images(self) -> Iterator[Image]:
        if not self.capture.isOpened():
            raise Exception('Error:cannot opening video stream or file')
        while self.capture.isOpened():
            ret, frame = self.capture.read()
            if ret:
                yield Image(frame, imagelib.image.color_models.BGRColor())
            else:
                break
