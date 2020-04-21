from dataclasses import dataclass
from math import inf

import cv2

from .point import Point
from ..draw import Brush, Drawable, BrushFactory
from ..image import Image


@dataclass
class Line(Drawable):
    point1: Point
    point2: Point

    def slope(self) -> float:
        diff = self.point1 - self.point2
        return diff.y / diff.x if diff.x != 0 else inf

    def length(self) -> float:
        return self.point1.distance_to(self.point2)

    def draw(self, image: Image, brush: Brush = BrushFactory().get_default_brush()) -> Image:
        image_data = image.clone().to_numpy()
        point1 = self.point1.to_grid_tuple()
        point2 = self.point2.to_grid_tuple()
        cv2.line(image_data, point1, point2, brush.color, brush.thickness)
        return Image(image_data, image.color_model)

    def __str__(self) -> str:
        return f'({self.point1} --- {self.point2})'

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other: 'Line') -> bool:
        return self.point1 == other.point1 and self.point2 == other.point2
