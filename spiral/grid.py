class Grid:
    @property
    def width(self):
        raise NotImplementedError

    @property
    def height(self):
        raise NotImplementedError

    def content_at(self, x: int, y: int) -> str:
        raise NotImplementedError
