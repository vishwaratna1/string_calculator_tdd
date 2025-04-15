from tests.fixtures.calculator_fixtures import calculator

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

