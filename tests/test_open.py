import pytest
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
def test_number_addition():
    assert number_addition(9999, -9999) == 0
