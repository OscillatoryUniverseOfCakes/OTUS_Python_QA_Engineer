class Figure:
    NEEDED_SIDES = -1

    @property
    def perimeter(self):
        raise NotImplemented('Свойство ещё не объявлено')

    @property
    def area(self):
        raise NotImplemented('Свойство ещё не объявлено')

    def __init__(self, *args):
        if len(args) == self.NEEDED_SIDES and self.is_positive(args):
            self.sides = args
        else:
            raise ValueError

    def add_area(self, figure: object):
        if isinstance(figure, Figure) and (isinstance(figure.area, float) or isinstance(figure.area, int)):
            return self.area + figure.area
        else:
            raise ValueError

    @staticmethod
    def is_positive(args):
        for arg in args:
            if arg <= 0:
                return False
        return True
