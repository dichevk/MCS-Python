import random
from main import is_bet_even_or_odd

def test_is_bet_even_or_odd_even():
    random.seed(1)
    assert is_bet_even_or_odd("even") is True
    random.seed(50)
    assert is_bet_even_or_odd("even") is True

def test_is_bet_even_or_odd_odd():
    random.seed(2)
    assert is_bet_even_or_odd("odd") is False

def test_is_bet_even_or_odd_invalid_input():
    assert is_bet_even_or_odd("invalid") == "invalid input"

def test_is_bet_even_or_odd_eleven():
    assert is_bet_even_or_odd("odd") is False

def test_is_bet_even_or_odd_ten():
    assert is_bet_even_or_odd("even") is False
