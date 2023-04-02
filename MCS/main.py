import random
from typing import List, Union

final_funds: List[float] = []


def is_bet_even_or_odd(choice: str) -> Union[bool, str]:
    note = random.randint(1, 100)
    if choice.lower() == "even":
        if note % 2 != 0 or note == 10:
            return False
        elif note % 2 == 0:
            return True
    elif choice.lower() == "odd":
        if note % 2 == 0 or note == 11:
            return False
        elif note % 2 == 1:
            return True
    else:
        return "invalid input"


def play(total_money: float, bet_money: float, total_plays: int, input_string: str) -> Union[List[float], None, str]:
    if not isinstance(total_money, (float, int)):
        raise TypeError("total_money must be a number")
    if not isinstance(bet_money, (float, int)):
        raise TypeError("bet_money must be a number")
    if not isinstance(total_plays, int):
        raise TypeError("total_plays must be an integer")
    if total_plays <= 0:
        return []
    if is_bet_even_or_odd(input_string) == "invalid input":
        print("The input was invalid, please use even or odd")
        return None
    if total_money <= 0 or bet_money <= 0:
        print("Cannot bet with no money")
        return None

    num_of_plays: List[int] = []
    money: List[float] = []

    play_amount = 1

    for play_amount in range(total_plays):
        # we win
        if is_bet_even_or_odd(input_string) == "invalid input":
            print("The input was invalid, please use even or odd")
            return
        if is_bet_even_or_odd(input_string):
            # Add the money to the fund
            total_money = total_money + bet_money
        # we lose
        else:
            total_money = total_money - bet_money
        # Add the play number
        num_of_plays.append(play_amount)
        # Add the new fund amount
        money.append(total_money)

    # Add the final fund to the final_funds list
    final_funds.append(money[-1])

    return final_funds


def run_casino(num_iterations: int, total_money: float, bet_money: float, number_of_bets: int) -> Union[List[float], None, str]:
    user_input = input("Please choose if you want to bet on even or odd  \n ")
    print("run with" + " " + str(num_iterations) + " " + "num of iterations")
    ending_fund = []
    if num_iterations == 0 or number_of_bets == 0:
        return None
    if total_money<=0 or bet_money<=0:
        return None
    for i in range(num_iterations):
        ending_fund.append(play(total_money, bet_money, number_of_bets, user_input)[0])
    print("the player started with " + "" + str(total_money))
    avg_ending_fund = sum(ending_fund) / len(ending_fund)
    print("the Player has this amount left: ", str(avg_ending_fund))
    return ending_fund


