from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from imagelib.image import NamedWindow
from imagelib.patterns import Singleton
from imagelib.video import Video

if TYPE_CHECKING:
    from imagelib.image import Image


class VideoPlayer:
    _state: 'VideoPlayerState'
    _window: NamedWindow
    _video: Video
    _position: int = 0

    def __init__(self, video: Video, window: NamedWindow):
        self._video = video
        self._window = window
        self._state = Playing()

    def tick(self):
        self._state.tick(self)

    def toggle(self):
        self._state.toggle(self)

    def forward(self):
        self._state.forward(self)

    def backward(self):
        self._state.backward(self)

    def close(self):
        self._state.close(self)

    def get_frame(self) -> 'Image':
        return self._video[self.position]

    @property
    def is_end(self) -> bool:
        return self.position == len(self._video) - 1

    @property
    def is_start(self) -> bool:
        return self.position == 0

    @property
    def closed(self) -> bool:
        return self._state == Closed()

    @property
    def window(self) -> NamedWindow:
        return self._window

    @property
    def video(self) -> Video:
        return self._video

    @property
    def position(self) -> int:
        return self._position

    @position.setter
    def position(self, value: int):
        self._position = value


class VideoPlayerState(ABC, Singleton):
    @abstractmethod
    def tick(self, ctx: VideoPlayer):
        pass

    @abstractmethod
    def toggle(self, ctx: VideoPlayer):
        pass

    @abstractmethod
    def forward(self, ctx: VideoPlayer):
        pass

    @abstractmethod
    def backward(self, ctx: VideoPlayer):
        pass

    @abstractmethod
    def close(self, ctx: VideoPlayer):
        pass


class AbstractVideoPlayerState(VideoPlayerState):
    def tick(self, ctx: VideoPlayer):
        ctx.get_frame().show(ctx.window)

    def toggle(self, ctx: VideoPlayer):
        pass

    def forward(self, ctx: VideoPlayer):
        if not ctx.is_end:
            ctx.position += 1

    def backward(self, ctx: VideoPlayer):
        if not ctx.is_start:
            ctx.position -= 1

    def close(self, ctx: VideoPlayer):
        ctx._state = Closed()


class Playing(AbstractVideoPlayerState):
    def tick(self, ctx: VideoPlayer):
        super().tick(ctx)
        ctx.forward()

    def toggle(self, ctx: VideoPlayer):
        ctx._state = Stopped()


class Stopped(AbstractVideoPlayerState):
    def toggle(self, ctx: VideoPlayer):
        ctx._state = Playing()


class Closed(AbstractVideoPlayerState):
    pass
