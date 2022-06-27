import pytest


def test_add_area_err(default_triangle):
    class Food:
        pass

    with pytest.raises(ValueError):
        default_triangle.add_area(Food())


def test_add_area_1(default_triangle, default_square):
    assert default_triangle.add_area(default_square) == 184


def test_add_area_2(default_rectangle, default_square):
    assert default_rectangle.add_area(default_square) == 300


def test_add_area_3(default_square):
    assert default_square.add_area(default_square) == 200


def test_add_area_4(default_circle, default_square):
    assert default_circle.add_area(default_square) - 414 < 0.000001
