import cv2
import numpy as np

from ..bounding_box import BoundingBox
from ..image import Image
from ..lib import Brush, Point, BrushFactory


class RectBoundingBox(BoundingBox):
    def __init__(self, p1: Point, p2: Point):
        self._p1 = p1
        self._p2 = p2

    @property
    def point_min(self) -> Point:
        return self._p1

    @point_min.setter
    def point_min(self, value: Point):
        self._p1 = value

    @property
    def point_max(self) -> Point:
        return self._p2

    @point_max.setter
    def point_max(self, value: Point):
        self._p2 = value

    @property
    def center_point(self) -> Point:
        return Point(
            (self._p1.x + self._p2.x) / 2,
            (self._p1.y + self._p2.y) / 2
        )

    @property
    def width(self):
        return self.point_max.x - self.point_min.x + 1

    @property
    def height(self):
        return self.point_max.y - self.point_min.y + 1

    @property
    def area(self):
        return self.width * self.height

    def draw_to_image(
            self,
            image: Image,
            brush: Brush = BrushFactory().get_default_brush()
    ) -> Image:
        """
        Return a new Image that has a bounding box on it.
        """
        data = image.clone().to_numpy()
        cv2.rectangle(
            data,
            (self._p1.x, self._p1.y),
            (self._p2.x, self._p2.y),
            brush.color,
            brush.thickness
        )
        return Image(data, image.color_model)

    def crop_image(self, image: Image):
        data = image.clone().to_numpy()
        data = data[self.point_min.y: self.point_max.y + 1, self.point_min.x: self.point_max.x + 1]
        return Image(data, image.color_model)

    def is_in_distance_of(self, point: Point, distance: float) -> bool:
        """
        Return True if the distance to the center of bounding box less than specify distance.
        """
        return point.distance_to(self.center_point) <= distance

    def merge_with(self, other: 'RectBoundingBox') -> 'RectBoundingBox':
        """
        Merge two bounding boxes, and return a new instance of the merged bounding box.
        """
        x1 = min(self.point_min.x, other.point_min.x)
        y1 = min(self.point_min.y, other.point_min.y)

        x2 = max(self.point_max.x, other.point_max.x)
        y2 = max(self.point_max.y, other.point_max.y)

        return RectBoundingBox(Point(x1, y1), Point(x2, y2))

    def to_numpy_as_yolo_form(self, image: Image) -> np.ndarray:  # TODO extract this method as strategy pattern
        """
        BoundingBox in this class is store as (x_min, y_min, x_max, y_max) form
        This method will return a np array with (x_center, y_center, width, height) form
        """

        x_center = (self.point_min.x + self.width / 2) / image.width
        y_center = (self.point_min.y + self.height / 2) / image.height
        width = self.width / image.width
        height = self.height / image.height
        return np.array([x_center, y_center, width, height])

    def __str__(self) -> str:
        return '{%s, %s}' % (self.point_min, self.point_max)
