from typing import List

from spiral.grid import Grid


def print_grid(grid: Grid, labels: bool = False) -> str:
    pad = 1 if not labels else max(len(f'{grid.width}'), len(f'{grid.height}'))

    all_content = _header(grid.width, pad, labels) + \
                  [_row(i, row, pad, labels) for i, row in enumerate(grid)]

    return '\n'.join(' '.join(row) for row in all_content).rstrip()


def _header(width, pad, labels=False):
    return [[' ' * pad] + [f'{i:{pad}}' for i in range(width)]] if labels else []


def _row(index, row, pad, labels=False):
    return ([f'{index:{pad}}'] if labels else []) + [f'{v:{pad}}' for v in row]


def _fill(rows, cols, value=1) -> List[List[int]]:
    return [[value] * cols for _ in range(rows)]


def _build_spiral(size: int) -> List[List[int]]:
    fill = _fill(size, size)

    last_y = size // 2
    last_x = (size // 2 - 1) if size % 2 == 0 else size // 2

    if size == 5:
        last_x = 1
        last_y = 3
    elif (size - 5) % 4 == 0:
        last_x -= 1
        last_y += 1

    x = 0
    y = 1
    dir_x = 1
    dir_y = 0
    left_border = 0
    right_border = size - 1
    upper_border = 0
    lower_border = size - 1

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
        elif x == right_border - 1 and y == lower_border:
            y -= 1
            x -= 1
            dir_x = -1
            dir_y = 0
            right_border -= 2
        elif x == left_border + 1 and y == upper_border:
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
    return fill
