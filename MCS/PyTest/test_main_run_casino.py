import pytest
from main import run_casino
import random


def test_run_casino_valid_input():
    assert run_casino(1, 100, 10, 5) is not None


def test_run_casino_invalid_input():
    assert run_casino(1, 100, 10, 5) is not None


def test_run_casino_invalid_types():
    with pytest.raises(TypeError):
        run_casino(1, "100", 10, 5)

def test_run_casino_invalid_number_of_bets():
    with pytest.raises(TypeError):
        run_casino(1, 100, 10, 5.643)

def test_run_casino_zero_iterations():
    assert run_casino(0, 100, 10, 5) is None


def test_run_casino_negative_money():
    assert run_casino(1, -100, 10, 5) is None


def test_run_casino_negative_bet():
    assert run_casino(1, -100, -10, 5) is None
