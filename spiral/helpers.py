from typing import List

from spiral.grid import Grid


def print_grid(grid: Grid, labels: bool = False) -> str:
    field_width = 1 if not labels else max(len(f'{grid.width}'), len(f'{grid.height}'))
    all_content = []

    if labels:
        header_row = [''.ljust(field_width, ' ')]
        for i in range(grid.width):
            header_row.append(f'{i}'.ljust(field_width, ' '))
        all_content.append(header_row)

    for j in range(grid.height):
        row_contents = []
        if labels:
            y_coords = f'{j}'.ljust(field_width, ' ')
            row_contents.append(y_coords)
        for i in range(grid.width):
            row_contents.append(grid[i, j].ljust(field_width, ' '))
        all_content.append(row_contents)
    return '\n'.join(' '.join(row) for row in all_content).rstrip()


def _fill(arr: List[List[int]], value=1) -> List[List[int]]:
    return [[value for _ in row] for row in arr]


def _build_spiral(size: int) -> List[List[int]]:
    arr = [[0] * size for _ in range(size)]
    fill = _fill(arr)
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
