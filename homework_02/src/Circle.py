from homework_02.src.Figure import Figure


class Circle(Figure):
    NAME = 'Круг'
    NEEDED_SIDES = 1

    @property
    def perimeter(self):
        return 2 * 3.14 * self.sides[0]

    @property
    def area(self):
        return 3.14 * (self.sides[0] ** 2)
