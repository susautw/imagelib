from dataclasses import dataclass
from math import sqrt
from typing import Tuple

import cv2

from ..draw import Brush, Drawable, BrushFactory
from ..image import Image


@dataclass
class Point(Drawable):
    x: float
    y: float

    def to_tuple(self) -> Tuple[float, float]:
        return self.x, self.y

    def to_grid_tuple(self) -> Tuple[int, int]:
        return int(self.x), int(self.y)

    def distance_to(self, point: 'Point') -> float:
        diff = self - point
        return sqrt(diff.x ** 2 + diff.y ** 2)

    def draw(self, image: Image, brush: Brush = BrushFactory().get_default_brush()):
        image_data = image.clone().to_numpy()
        cv2.circle(image_data, self.to_grid_tuple(), brush.thickness, brush.color)
        return Image(image_data, image.color_model)

    def __add__(self, other: 'Point') -> 'Point':
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Point') -> 'Point':
        return Point(self.x - other.x, self.y - other.y)

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other: 'Point') -> bool:
        return self.x == other.x and self.y == other.y
