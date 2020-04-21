import cv2

from ..axis import Point


class NamedWindow:
    _name: str

    def __init__(self, name: str, flag=cv2.WINDOW_NORMAL):
        self._name = name
        cv2.namedWindow(name, flag)

    @property
    def name(self):
        return self._name

    def resize(self, width: int, height: int) -> None:
        cv2.resizeWindow(self.name, width, height)

    def move(self, point: Point) -> None:
        cv2.moveWindow(self.name, point.x, point.y)

    def destroy(self) -> None:
        cv2.destroyWindow(self.name)

    @staticmethod
    def destroy_all() -> None:
        cv2.destroyAllWindows()
