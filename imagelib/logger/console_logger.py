import sys

from imagelib.logger import Logger
from imagelib.patterns import Singleton


class ConsoleLogger(Logger, Singleton):
    def log(self, msg: str) -> None:
        print(msg)

    def info(self, msg: str) -> None:
        print(f'[info] {msg}')

    def debug(self, msg: str) -> None:
        print(f'[debug] {msg}')

    def error(self, msg: str) -> None:
        print(f'[error] {msg}', file=sys.stderr)
