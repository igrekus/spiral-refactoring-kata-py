from spiral.grid import Grid


class GridPrinter:
    @staticmethod
    def print(grid: Grid, labels: bool = False) -> str:
        field_width = max(len(f'{grid.width}'), len(f'{grid.height}'))
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
                row_contents.append(grid.content_at(i, j).ljust(field_width, ' '))
            all_content.append(row_contents)
        return '\n'.join(' '.join(row) for row in all_content)
