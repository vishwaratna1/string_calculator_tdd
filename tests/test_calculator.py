from tests.fixtures.calculator_fixtures import calculator

def test_empty_string_returns_zero(calculator):
    assert calculator.add("") == 0

