import pytest
from src.Circle import Circle


def test_circl_creat_err_redudant_1():
    with pytest.raises(ValueError):
        Circle()


def test_circl_creat_err_redudant_2():
    with pytest.raises(ValueError):
        Circle(1, 2)


def test_circl_creat_err_negative():
    with pytest.raises(ValueError):
        Circle(-1)


def test_circl_creat_err_zero():
    with pytest.raises(ValueError):
        Circle(0)


def test_circl_perimeter(default_circle):
    assert default_circle.perimeter - 62.8 < 0.0000001


def test_circl_area(default_circle):
    assert default_circle.area - 314 < 0.0000001


def test_circl_name(default_circle):
    assert default_circle.NAME == 'Круг'
