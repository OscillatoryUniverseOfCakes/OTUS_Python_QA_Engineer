import pytest

from src.Triangle import Triangle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Circle import Circle


@pytest.fixture
def default_triangle():
    triangle = Triangle(13, 14, 15)
    yield triangle
    del triangle


@pytest.fixture
def default_rectangle():
    rectangle = Rectangle(10, 20)
    yield rectangle
    del rectangle


@pytest.fixture
def default_square():
    square = Square(10)
    yield square
    del square


@pytest.fixture
def default_circle():
    circle = Circle(10)
    yield circle
    del circle
