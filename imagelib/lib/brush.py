from dataclasses import dataclass
from typing import Tuple

from ..patterns import Singleton


@dataclass
class Brush:
    color: Tuple[int, int, int]
    thickness: int


class BrushFactory(Singleton):
    def get_default_brush(self) -> Brush:
        return Brush((50, 50, 255), 3)
