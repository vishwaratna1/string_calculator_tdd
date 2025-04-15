import pytest
from calculator.app import StringCalculator

@pytest.fixture
def calculator():
    return StringCalculator()