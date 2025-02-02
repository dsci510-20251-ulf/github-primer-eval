import pytest
import math
from lab_primer import number_addition


@pytest.mark.timeout(0.3)
def test_number_addition_positive_integers():
    assert number_addition(2, 3) == 5


@pytest.mark.timeout(0.3)
def test_number_addition_negative_integers():
    assert number_addition(-2, -3) == -5


@pytest.mark.timeout(0.3)
def test_number_addition_mixed_integers():
    assert number_addition(-2, 3) == 1


@pytest.mark.timeout(0.3)
def test_number_addition_floats():
    assert number_addition(2.5, 3.1) == 5.6


@pytest.mark.timeout(0.3)
def test_number_addition_float_integer():
    assert number_addition(1, 2.6) == 3.6


@pytest.mark.timeout(0.3)
def test_number_addition_failure():
    # purposely failed for github classroom demo
    assert number_addition(9999, -9999) == -1


@pytest.mark.timeout(0.3)
def test_number_addition_one_input_zero():
    assert number_addition(-3, 0) == -3


@pytest.mark.timeout(0.3)
def test_number_addition_small_numbers():
    assert number_addition(1e-10, 1e-10) == 2e-10


@pytest.mark.timeout(0.3)
def test_number_addition_nan():
    assert math.isnan(number_addition(math.nan, 1))


@pytest.mark.timeout(0.3)
def test_number_addition_minus_inf_plus_inf():
    assert math.isnan(number_addition(-math.inf, math.inf))
