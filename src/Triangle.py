from src.Figure import Figure


class Triangle(Figure):
    NAME = 'Треугольник'
    NEEDED_SIDES = 3

    @property
    def perimeter(self):
        return sum(self.sides)

    @property
    def area(self):
        p = self.perimeter / 2
        return (p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2])) ** 0.5
