from flask import Flask, jsonify, request
from typing import List, Union
import random
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///casino.db'
db = SQLAlchemy(app)

class Play(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    total_money = db.Column(db.Float)
    bet_money = db.Column(db.Float)
    total_plays = db.Column(db.Integer)
    input_string = db.Column(db.String(10))
    ending_fund = db.Column(db.Float)

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

    # Add the final fund to the database
    ending_fund = money[-1]
    db.session.add(Play(total_money=total_money, bet_money=bet_money, total_plays=total_plays, input_string=input_string, ending_fund=ending_fund))
    db.session.commit()

    return {"ending_fund": ending_fund}


@app.route('/play', methods=['POST'])
def play_endpoint():
    data = request.get_json()
    try:
        response = play(data['total_money'], data['bet_money'], data['total_plays'], data['input_string'])
        if response is not None:
            return jsonify(response)
        else:
            return "Bad request parameters", 400
    except TypeError as e:
        return str(e), 400


if __name__ == '__main__':
    app.run(debug=True)

