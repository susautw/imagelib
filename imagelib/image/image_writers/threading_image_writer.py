from concurrent.futures.thread import ThreadPoolExecutor
from pathlib import Path
from typing import TYPE_CHECKING

import cv2

from ...image.image_writers import ImageWriter

if TYPE_CHECKING:
    from imagelib.image import Image


class ThreadingImageWriter(ImageWriter):
    def __init__(self, max_workers=100):
        self.executor = ThreadPoolExecutor(max_workers=max_workers)

    def wait(self):
        self.executor.shutdown()

    def write(self, image: 'Image', path: Path):
        assert not path.is_file(), f'{str(Path)} :the file exists.'

        def job():
            cv2.imencode('.jpg', image.to_numpy())[1].tofile(str(path))

        self.executor.submit(job)

    def __del__(self):
        self.wait()
