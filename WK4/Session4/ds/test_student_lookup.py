# test_student_lookup.py

import pytest
import student_lookup as sl


def test_find_mark_known_student():
    students = {"Aisha": 85, "Bilal": 72, "Chen": 90}
    result = sl.find_mark(students, "Aisha")
    assert result == 85, (
        "find_mark should return the student's mark for a known name; "
        f"expected 85 for 'Aisha', but got {result}"
    )


def test_find_mark_unknown_student():
    students = {"Aisha": 85, "Bilal": 72, "Chen": 90}
    result = sl.find_mark(students, "Dina")
    assert result is None, (
        "find_mark should return None for an unknown name; "
        f"expected None for 'Dina', but got {result}"
    )


def test_find_mark_other_known_student():
    students = {"Aisha": 85, "Bilal": 72, "Chen": 90}
    result = sl.find_mark(students, "Chen")
    assert result == 90, (
        "find_mark should return the correct mark for 'Chen'; "
        f"expected 90, but got {result}"
    )


@pytest.mark.parametrize("bad_students", [
    ["Aisha", "Bilal"],   # list instead of dict
    "not a dict",
    None
])
def test_find_mark_invalid_students_type_raises_type_error(bad_students):
    with pytest.raises(TypeError):
        sl.find_mark(bad_students, "Aisha")  # type: ignore


@pytest.mark.parametrize("bad_name", [123, None, ["Aisha"]])
def test_find_mark_invalid_name_type_raises_type_error(bad_name):
    students = {"Aisha": 85}
    with pytest.raises(TypeError):
        sl.find_mark(students, bad_name)  # type: ignore