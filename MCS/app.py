from flask import Flask, request, jsonify, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
import random
from typing import List, Union

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class CasinoBet(db.model):
    id = db.Column(db.Integer, primary_key=True)
    total_money = db.Column(db.Float,nullable=False)
    bet_money = db.Column(db.Float, nullable=False)
    number_of_bets = db.Column(db.Integer, nullable=False)
    user_input = db.Column(db.String, nullable=False)
    num_iterations = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return '<CasinoBet %r>' %self.id


final_funds: List[float] = []
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

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
        return None
    if total_money <= 0 or bet_money <= 0:
        return None

    num_of_plays: List[int] = []
    money: List[float] = []

    play_amount = 1

    for play_amount in range(total_plays):
        # we win
        if is_bet_even_or_odd(input_string) == "invalid input":
            return None
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


@app.route('/casino', methods=['POST'])
def run_casino():
    data = request.json
    num_iterations = data['num_iterations']
    total_money = data['total_money']
    bet_money = data['bet_money']
    number_of_bets = data['number_of_bets']
    user_input = data['user_input']
    print("run with" + " " + str(num_iterations) + " " + "num of iterations")
    ending_fund = []
    if num_iterations == 0 or number_of_bets == 0:
        return jsonify(error="Invalid input: num_iterations and number_of_bets must be greater than zero")
    if total_money <= 0 or bet_money <= 0:
        return jsonify(error="Invalid input: total_money and bet_money must be greater than zero")
    for i in range(num_iterations):
        ending_fund.append(play(total_money, bet_money, number_of_bets, user_input)[0])
    print("the player started with " + "" + str(total_money))
    avg_ending_fund = sum(ending_fund) / len(ending_fund)
    return jsonify(ending_fund=ending_fund, avg_ending_fund=avg_ending_fund)
