import cv2

from ..axis import BoundingBox, Point
from imagelib.image import NamedWindow, Image


def select_roi(window: NamedWindow, image: Image) -> BoundingBox:
    x1, y1, w, h = cv2.selectROI(window.name, image.to_numpy())
    if w == 0 or h == 0:
        raise Exception('no selection')
    return BoundingBox(
        Point(x1, y1),
        Point(x1 + w - 1, y1 + h - 1)
    )
