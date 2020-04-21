from typing import Iterable, List

from ..image import Image
from ..axis import Point, Line
from ..draw import Drawable, Brush, BrushFactory


class PathCurve(Drawable):
    _points: Iterable[Point]
    _lines: List[Line]

    def __init__(self, points: Iterable[Point]):
        self._points = points
        self._build_lines()

    def _build_lines(self) -> None:
        self._lines = [Line(p1, p2) for p1, p2 in zip(self._points[:-1], self._points[1:])]

    def draw(self, image: Image, brush: Brush = BrushFactory().get_default_brush()) -> Image:
        for line in self._lines:
            image = line.draw(image, brush)
        return image

    def __getitem__(self, item) -> Point:
        return self._points[item]

    @property
    def lines(self) -> List[Line]:
        return self._lines
