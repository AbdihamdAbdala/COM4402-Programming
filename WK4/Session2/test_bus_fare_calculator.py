# test_bus_fare_calculator.py

import pytest
import math
import bus_fare_calculator as bf


# -------- get_fare valid cases --------

@pytest.mark.parametrize("age, is_peak, expected", [
    # Adult peak / off-peak
    (30, True, 2.50),
    (30, False, 2.50 * 0.8),

    # Child (<16) peak / off-peak
    (0, True, 1.25),              # border lower
    (10, True, 1.25),
    (15, False, 1.25 * 0.8),

    # Senior (65+) peak / off-peak
    (65, True, 1.00),
    (80, False, 1.00 * 0.8),
])
def test_get_fare_valid_and_border(age, is_peak, expected):
    result = bf.get_fare(age, is_peak)
    assert math.isclose(result, expected, rel_tol=1e-3), (
        f"get_fare({age}, {is_peak}) should be about {expected}, "
        f"but got {result}"
    )


# -------- get_fare invalid age --------

@pytest.mark.parametrize("bad_age", [-1, -10])
def test_get_fare_negative_age_raises_value_error(bad_age):
    with pytest.raises(ValueError):
        bf.get_fare(bad_age, True)


# -------- get_fare invalid types --------

@pytest.mark.parametrize("bad_age", ["20", 20.5, None])
def test_get_fare_invalid_age_type_raises_type_error(bad_age):
    with pytest.raises(TypeError):
        bf.get_fare(bad_age, True)  # type: ignore


@pytest.mark.parametrize("bad_peak", ["yes", 1, None])
def test_get_fare_invalid_is_peak_type_raises_type_error(bad_peak):
    with pytest.raises(TypeError):
        bf.get_fare(30, bad_peak)  # type: ignore