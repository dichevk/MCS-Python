from main import play
import pytest
import random


def test_play_with_invalid_input():
    # Test with invalid input
    assert play(100, 10, 1, "invalid") is None


def test_play_returns_list():
    assert isinstance(play(100, 10, 1, "even"), list)


def test_play_returns_non_negative_final_fund():
    assert play(100, 10, 1, "even")[0] >= 0


def test_play_returns_none_when_input_string_is_invalid():
    assert play(100, 10, 1, "invalid input") is None


def test_play_raises_type_error_when_total_money_is_not_a_number():
    with pytest.raises(TypeError):
        play("100", 10, 1, "even")


def test_play_raises_type_error_when_bet_money_is_not_a_number():
    with pytest.raises(TypeError):
        play(100, "10", 1, "even")


def test_play_raises_type_error_when_total_plays_is_not_a_number():
    with pytest.raises(TypeError):
        play(100, 10, "5", "even")


def test_play_invalid_input():
    assert play(100, 10, 1, "invalid") is None


def test_play_zero_total_plays():
    assert play(100, 10, 0, "even") == []

def test_play_negative_total_money():
    assert play(-100, 10, 1, "even" or "odd") is None

def test_play_negative_total_bet():
    assert play(100, -10, 1, "even" or 'odd') is None
