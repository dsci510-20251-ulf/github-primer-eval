import pytest
import math
from lab_primer import number_addition


@pytest.mark.timeout(0.3)
def test_number_addition_1():
    assert number_addition(2, 3) == 5


@pytest.mark.timeout(0.3)
def test_number_addition_2():
    assert number_addition(-2, -3) == -5


@pytest.mark.timeout(0.3)
def test_number_addition_3():
    assert number_addition(-2, 3) == 1


@pytest.mark.timeout(0.3)
def test_number_addition_4():
    assert number_addition(2.5, 3.1) == 5.6


@pytest.mark.timeout(0.3)
def test_number_addition_5():
    assert number_addition(1, 2.6) == 3.6


@pytest.mark.timeout(0.3)
def test_number_addition_6():
    # purposely failed for github classroom demo
    assert number_addition(9999, -9999) == 0


@pytest.mark.timeout(0.3)
def test_number_addition_7():
    assert number_addition("cat", "dog") is None


@pytest.mark.timeout(0.3)
def test_number_addition_8():
    assert number_addition(1e-10, 1e-10) == 2e-10


@pytest.mark.timeout(0.3)
def test_number_addition_9():
    assert math.isnan(number_addition(math.nan, 1))


@pytest.mark.timeout(0.3)
def test_number_addition_10():
    assert math.isnan(number_addition(-math.inf, math.inf))
