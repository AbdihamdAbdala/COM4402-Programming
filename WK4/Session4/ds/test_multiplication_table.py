# test_multiplication_table.py

import pytest
import multiplication_table as mt


def test_multiplication_table_zero():
    result = mt.multiplication_table(0)
    assert result == [], (
        "multiplication_table(0) should return an empty list, but got "
        f"{result}"
    )


def test_multiplication_table_one():
    result = mt.multiplication_table(1)
    assert result == [[1]], (
        "multiplication_table(1) should return [[1]], but got "
        f"{result}"
    )


def test_multiplication_table_three():
    result = mt.multiplication_table(3)
    expected = [
        [1, 2, 3],
        [2, 4, 6],
        [3, 6, 9],
    ]
    assert result == expected, (
        "multiplication_table(3) should return "
        "[[1, 2, 3], [2, 4, 6], [3, 6, 9]], but got "
        f"{result}"
    )


@pytest.mark.parametrize("bad_n", [-1, -5])
def test_multiplication_table_negative_raises_value_error(bad_n):
    with pytest.raises(ValueError):
        mt.multiplication_table(bad_n)


@pytest.mark.parametrize("bad_type", [2.5, "3", None, [3]])
def test_multiplication_table_invalid_type_raises_type_error(bad_type):
    with pytest.raises(TypeError):
        mt.multiplication_table(bad_type)  # type: ignore