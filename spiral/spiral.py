from typing import List, Optional

from spiral.grid import Grid
from spiral.gridprinter import GridPrinter


class Spiral(Grid):
    def __init__(self, size: int):
        self._size: int = size

    @property
    def width(self) -> int:
        return self._size

    @property
    def height(self) -> int:
        return self._size

    def content_at(self, x: int, y: int) -> str:
        s = self._spiralize()
        return '' if not s else f'{s[y][x]}'

    def print(self) -> str:
        return GridPrinter.print(self, False).rstrip()

    def _spiralize(self, arr=None) -> Optional[List[List[int]]]:
        if arr is None:
            return None if self._size < 5 else self._spiralize([[0] * self._size for _ in range(self._size)])

        fill = self._fill(arr)
        height: int = len(fill)
        width: int = len(fill[0])
        last_y = height // 2
        last_x = (width // 2 - 1) if width % 2 == 0 else width // 2

        if height == 5:
            last_x = 1
            last_y = 3
        elif (height - 5) % 4 == 0:
            last_x -= 1
            last_y += 1

        x = 0
        y = 1
        dir_x = 1
        dir_y = 0
        i = 0
        left_border = 0
        right_border = width - 1
        upper_border = 0
        lower_border = height - 1

        while True:
            if x == right_border and y == upper_border + 1:
                x -= 1
                y += 1
                dir_x = 0
                dir_y = 1
                upper_border += 2
            elif x == left_border and y == lower_border - 1:
                x += 1
                y -= 1
                dir_x = 0
                dir_y = -1
                lower_border -= 2
            elif y == lower_border and x == right_border - 1:
                y -= 1
                x -= 1
                dir_x = -1
                dir_y = 0
                right_border -= 2
            elif y == upper_border and x == left_border + 1:
                y += 1
                x += 1
                dir_x = 1
                dir_y = 0
                left_border += 2
            fill[y][x] = 0
            if y == last_y and x == last_x:
                break

            x += dir_x
            y += dir_y
            i += 1
        return fill

    def _fill(self, arr: List[List[int]]) -> List[List[int]]:
        return [[1 for _ in row] for row in arr]
