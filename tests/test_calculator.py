import pytest
from tests.fixtures.calculator_fixtures import calculator
from calculator.app import NegativeNumberException

def test_empty_string_returns_zero(calculator):
    assert calculator.add("") == 0

def test_single_number_returns_itself(calculator):
    assert calculator.add("1") == 1

def test_multiple_comma_seperated_numbers_returns_sum(calculator):
    assert calculator.add("1,5,9") == 15

def test_multiple_comma_seperated_values_with_new_line_between_numbers(calculator):
    assert calculator.add("1\n2,3") == 6

def test_supports_custom_delimiter(calculator):
    assert calculator.add("//;\n1;2") == 3

def test_throw_exception_for_negative_numbers(calculator):
    with pytest.raises(NegativeNumberException) as excinfo:
        calculator.add("1,-2,3")
    assert "negative numbers not allowed: -2" in str(excinfo.value)

def test_get_called_count(calculator):
    calculator.add("1,2")
    calculator.add("3")
    assert calculator.get_called_count() == 2

def test_ignores_numbers_bigger_than_1000(calculator):
    assert calculator.add("2,1001") == 2


def test_supports_custom_delimiter_of_any_length(calculator):
    assert calculator.add("//[***]\n1***2***3") == 6
