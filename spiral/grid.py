class Grid:
    @property
    def width(self):
        raise NotImplementedError

    @property
    def height(self):
        raise NotImplementedError

    def __getitem__(self, item):
        raise NotImplementedError
