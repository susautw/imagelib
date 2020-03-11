from typing import TYPE_CHECKING

import cv2

from ..image.image_factorys import VideoCaptureImageFactory

if TYPE_CHECKING:
    from ..image import Image
    from ..image.image_iterator import ImageIterator


class Video:
    _fps: float
    _frames: 'ImageIterator'

    def __init__(self, fps: float, frames: 'ImageIterator'):
        self._frames = frames
        self._fps = fps

    @staticmethod
    def create_from_video_capture(cap: cv2.VideoCapture):
        fps = cap.get(cv2.CAP_PROP_FPS)
        frames = VideoCaptureImageFactory(cap).get()
        return Video(fps, frames)

    @staticmethod
    def create_from_image_iterator(image_iterator: 'ImageIterator', fps: float):
        return Video(fps, image_iterator)

    @property
    def fps(self) -> float:
        return self._fps

    def __len__(self):
        return len(self._frames)

    def __getitem__(self, item: int) -> 'Image':
        if item >= len(self):
            raise IndexError(f'video index out of bound {item}')
        return self._frames[item]
