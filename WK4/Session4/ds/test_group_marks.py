# test_group_marks.py

import pytest
import group_marks as gm


def test_group_marks_empty_list():
    result = gm.group_marks([])
    expected = {
        "Fail": [],
        "Pass": [],
        "Distinction": []
    }
    assert result == expected, (
        "group_marks([]) should return empty lists for all groups, but got "
        f"{result}"
    )


def test_group_marks_typical_case():
    marks = [20, 35, 40, 55, 72, 88]
    result = gm.group_marks(marks)
    expected = {
        "Fail": [20, 35],
        "Pass": [40, 55],
        "Distinction": [72, 88]
    }
    assert result == expected, (
        "group_marks([20, 35, 40, 55, 72, 88]) should group marks into "
        "{'Fail': [20, 35], 'Pass': [40, 55], 'Distinction': [72, 88]}, "
        f"but got {result}"
    )


def test_group_marks_border_values():
    marks = [0, 39, 40, 69, 70, 100]
    result = gm.group_marks(marks)
    expected = {
        "Fail": [0, 39],
        "Pass": [40, 69],
        "Distinction": [70, 100]
    }
    assert result == expected, (
        "group_marks border case failed; expected grouping into "
        f"{expected}, but got {result}"
    )


@pytest.mark.parametrize("bad_mark_list", [
    [-5, 50],      # negative mark
    [50, 120],     # > 100
])
def test_group_marks_out_of_range_raises_value_error(bad_mark_list):
    with pytest.raises(ValueError):
        gm.group_marks(bad_mark_list)


@pytest.mark.parametrize("bad_marks", [
    "not a list",
    123,
    None,
])
def test_group_marks_invalid_type_for_marks_raises_type_error(bad_marks):
    with pytest.raises(TypeError):
        gm.group_marks(bad_marks)  # type: ignore


def test_group_marks_invalid_element_type_raises_type_error():
    marks = [50, "60", 70]
    with pytest.raises(TypeError):
        gm.group_marks(marks)  # type: ignore