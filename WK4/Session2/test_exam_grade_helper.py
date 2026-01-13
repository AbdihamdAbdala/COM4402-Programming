# test_exam_grade_helper.py

import pytest
import exam_grade_helper as eg


# -------- classify_mark tests --------

@pytest.mark.parametrize("mark, expected", [
    (0, "Fail"),          # lower border
    (39, "Fail"),
    (40, "Pass"),         # pass border
    (69, "Pass"),
    (70, "Distinction"),  # distinction border
    (100, "Distinction"),
])
def test_classify_mark_valid_and_border(mark, expected):
    result = eg.classify_mark(mark)
    assert result == expected, (
        f"classify_mark({mark}) should be '{expected}', but got '{result}'"
    )


@pytest.mark.parametrize("bad_mark", [-1, -10, 101, 200])
def test_classify_mark_out_of_range_raises_value_error(bad_mark):
    with pytest.raises(ValueError):
        eg.classify_mark(bad_mark)


@pytest.mark.parametrize("bad_type", ["80", 75.5, None, [50]])
def test_classify_mark_invalid_type_raises_type_error(bad_type):
    with pytest.raises(TypeError):
        eg.classify_mark(bad_type)  # type: ignore


# -------- calculate_summary tests --------

def test_calculate_summary_typical_case():
    marks = [30, 40, 80]
    total, average, fail_count, distinction_count = eg.calculate_summary(marks)
    assert total == 150, (
        f"Total for {marks} should be 150, but got {total}"
    )
    assert average == pytest.approx(50.0), (
        f"Average for {marks} should be 50.0, but got {average}"
    )
    assert fail_count == 1, (
        f"Fail count for {marks} should be 1, but got {fail_count}"
    )
    assert distinction_count == 1, (
        f"Distinction count for {marks} should be 1, but got {distinction_count}"
    )


def test_calculate_summary_empty_list():
    marks = []
    total, average, fail_count, distinction_count = eg.calculate_summary(marks)
    assert total == 0, (
        f"Total for empty list should be 0, but got {total}"
    )
    assert average == pytest.approx(0.0), (
        f"Average for empty list should be 0.0, but got {average}"
    )
    assert fail_count == 0, (
        f"Fail count for empty list should be 0, but got {fail_count}"
    )
    assert distinction_count == 0, (
        f"Distinction count for empty list should be 0, but got {distinction_count}"
    )


@pytest.mark.parametrize("bad_marks", [
    [50, -1],       # out-of-range value
    [120],          # out-of-range value
])
def test_calculate_summary_out_of_range_marks_raise(bad_marks):
    with pytest.raises(ValueError):
        eg.calculate_summary(bad_marks)


@pytest.mark.parametrize("bad_marks", [
    "not a list",
    [50, "60"],
    None,
])
def test_calculate_summary_invalid_type_raises(bad_marks):
    with pytest.raises(TypeError):
        eg.calculate_summary(bad_marks)  # type: ignore