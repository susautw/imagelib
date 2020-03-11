from dataclasses import dataclass
from math import sqrt, inf
from typing import Tuple


class Point:
    _x: float
    _y: float

    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, value: float):
        self._x = value

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, value: float):
        self._y = value

    def to_tuple(self) -> Tuple[float, float]:
        return self.x, self.y

    def to_grid_tuple(self) -> Tuple[int, int]:
        return int(self.x), int(self.y)

    def distance_to(self, point: 'Point') -> float:
        return sqrt((point.x - self.x) ** 2 + (point.y - self.y) ** 2)

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


@dataclass(frozen=True)
class Line:
    point1: Point
    point2: Point

    def slope(self) -> float:
        diff = self.point1 - self.point2
        return diff.y / diff.x if diff.x != 0 else inf

    def length(self) -> float:
        diff = self.point1 - self.point2
        return sqrt(diff.x ** 2 + diff.y ** 2)

    def __str__(self) -> str:
        return f'({self.point1} --- {self.point2})'

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other: 'Line') -> bool:
        return self.point1 == other.point1 and self.point2 == other.point2

