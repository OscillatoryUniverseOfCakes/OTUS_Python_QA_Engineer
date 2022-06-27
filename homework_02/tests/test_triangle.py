import pytest
from homework_02.src.Triangle import Triangle


def test_tri_creat_err_redudant():
    with pytest.raises(ValueError):
        Triangle(1, 2, 3, 4)


def test_tri_creat_err_possibility():
    with pytest.raises(ValueError):
        Triangle(1, 2, 1000)


def test_tri_creat_err_negative_1():
    with pytest.raises(ValueError):
        Triangle(-1, -2, -3)


def test_tri_creat_err_negative_2():
    with pytest.raises(ValueError):
        Triangle(-1, -2, 3)


def test_tri_creat_err_negative_3():
    with pytest.raises(ValueError):
        Triangle(1, -2, -3)


def test_tri_creat_err_negative_4():
    with pytest.raises(ValueError):
        Triangle(-1, 2, 3)


def test_tri_creat_err_zero():
    with pytest.raises(ValueError):
        Triangle(1, 2, 0)


def test_tri_perimeter(default_triangle):
    assert default_triangle.perimeter == 42


def test_tri_area(default_triangle):
    assert default_triangle.area == 84


def test_tri_name(default_triangle):
    assert default_triangle.NAME == 'Треугольник'
