from spiral.grid import Grid
from spiral.helpers import print_grid, _build_spiral


class Spiral(Grid):
    def __init__(self, size: int):
        self._size = size
        self._spiral = '' if size < 5 else _build_spiral(size)

    @property
    def width(self) -> int:
        return self._size

    @property
    def height(self) -> int:
        return self._size

    def __getitem__(self, item):
        if isinstance(item, int):
            return self._spiral[item]

        if len(item) == 2 and all(isinstance(i, int) for i in item):
            x, y = item
            return '' if not self._spiral else f'{self._spiral[y][x]}'

    def __str__(self):
        return print_grid(self, False)
