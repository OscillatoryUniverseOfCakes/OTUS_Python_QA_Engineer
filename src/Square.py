from src.Figure import Figure


class Square(Figure):
    NAME = 'Квадрат'
    NEEDED_SIDES = 1

    @property
    def perimeter(self):
        return self.sides[0] * 4

    @property
    def area(self):
        return self.sides[0] ** 2
