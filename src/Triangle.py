from src.Figure import Figure


class Triangle(Figure):
    NAME = 'Треугольник'
    NEEDED_SIDES = 3

    def __init__(self, *args):
        super().__init__(*args)
        if not (self.sides[0] + self.sides[1] > self.sides[2] and
                self.sides[0] + self.sides[2] > self.sides[1] and
                self.sides[1] + self.sides[2] > self.sides[0]):
            raise ValueError

    @property
    def perimeter(self):
        return sum(self.sides)

    @property
    def area(self):
        p = self.perimeter / 2
        return (p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2])) ** 0.5
