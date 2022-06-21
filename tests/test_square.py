import pytest
from src.Square import Square


def test_sqr_creat_err_redudant_1():
    with pytest.raises(ValueError):
        Square()


def test_sqr_creat_err_redudant_2():
    with pytest.raises(ValueError):
        Square(1, 2)


def test_sqr_creat_err_negative():
    with pytest.raises(ValueError):
        Square(-1)


def test_sqr_creat_err_zero():
    with pytest.raises(ValueError):
        Square(0)


def test_sqr_perimeter(default_square):
    assert default_square.perimeter == 40


def test_sqr_area(default_square):
    assert default_square.area == 100


def test_sqr_name(default_square):
    assert default_square.NAME == 'Квадрат'
