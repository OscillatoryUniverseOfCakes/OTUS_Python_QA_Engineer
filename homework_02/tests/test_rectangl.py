import pytest
from homework_02.src.Rectangle import Rectangle


def test_rec_creat_err_redudant():
    with pytest.raises(ValueError):
        Rectangle()


def test_rec_creat_err_negative_1():
    with pytest.raises(ValueError):
        Rectangle(-1, -2)


def test_rec_creat_err_negative_2():
    with pytest.raises(ValueError):
        Rectangle(-1, 2)


def test_rec_creat_err_zero():
    with pytest.raises(ValueError):
        Rectangle(1, 0)


def test_rec_perimeter(default_rectangle):
    assert default_rectangle.perimeter == 60


def test_rec_area(default_rectangle):
    assert default_rectangle.area == 200


def test_rec_name(default_rectangle):
    assert default_rectangle.NAME == 'Четырехугольник'
