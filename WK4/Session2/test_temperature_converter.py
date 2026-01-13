# test_temperature_converter.py

import math
import pytest
import temperature_converter as tc


# -------- c_to_f tests --------

@pytest.mark.parametrize("celsius, expected", [
    (0.0, 32.0),          # freezing point
    (100.0, 212.0),       # boiling point
    (-40.0, -40.0),       # special point where C == F
    (37.0, 98.6),         # body temperature approx
])
def test_c_to_f_valid_and_border(celsius, expected):
    result = tc.c_to_f(celsius)
    assert math.isclose(result, expected, rel_tol=1e-3), (
        f"c_to_f({celsius}) should be about {expected}, but got {result}"
    )


@pytest.mark.parametrize("bad_value", [
    "not a number",
    None,
    [10],
])
def test_c_to_f_invalid_type_raises(bad_value):
    with pytest.raises(TypeError):
        tc.c_to_f(bad_value)  # type: ignore


# -------- f_to_c tests --------

@pytest.mark.parametrize("fahrenheit, expected", [
    (32.0, 0.0),          # freezing point
    (212.0, 100.0),       # boiling point
    (-40.0, -40.0),       # special point where C == F
    (98.6, 37.0),         # body temperature approx
])
def test_f_to_c_valid_and_border(fahrenheit, expected):
    result = tc.f_to_c(fahrenheit)
    assert math.isclose(result, expected, rel_tol=1e-3), (
        f"f_to_c({fahrenheit}) should be about {expected}, but got {result}"
    )


@pytest.mark.parametrize("bad_value", [
    "not a number",
    None,
    [32],
])
def test_f_to_c_invalid_type_raises(bad_value):
    with pytest.raises(TypeError):
        tc.f_to_c(bad_value)  # type: ignore