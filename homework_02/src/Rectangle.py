from homework_02.src.Figure import Figure


class Rectangle(Figure):
    NAME = 'Четырехугольник'
    NEEDED_SIDES = 2

    @property
    def perimeter(self):
        return sum(self.sides) * 2

    @property
    def area(self):
        return self.sides[0] * self.sides[1]
