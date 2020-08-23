from check_funcs import *
from deck import Deck
import random


"""
    Библиотека FLASK
"""
from flask import Flask, \
    render_template, \
    redirect, \
    request, \
    make_response, \
    jsonify

"""
    Запуск приложения FLASK
"""
application = Flask(__name__)

"""
    Настройка приложения для того, 
    чтобы можно было сохранять русские символы в json
"""
application.config.update(
    JSON_AS_ASCII=False
)


@application.route('/', methods=['GET', 'POST'])
def mainPage():
    pass


#application.run()


desk = Deck()

score_one = 0
score_two = 0
score_draw = 0
money_one_player = 0
money_two_player = 0
bet_one_player = 0
bet_two_player = 0

#bet_one_player = int(input('Игрок 1 введите свою ставку: '))
#bet_two_player = int(input('Игрок 2 введите свою ставку: '))

money_one_player -= bet_one_player
money_two_player -= bet_two_player

desk.new_game()
one_player = desk.get_cards_player()
two_player = desk.get_cards_player()
table = desk.get_cards_player(count=5)

print()

result = check_combinations(one_player + table)
result1 = check_combinations(two_player + table)

winner = change_winner(result, result1)
if winner[0] == 'F':
    score_one += 1
    money_one_player += bet_two_player + bet_one_player
    print(winner)
elif winner[0] == 'S':
    score_two += 1
    money_two_player += bet_two_player + bet_one_player
    print(winner)
else:
    score_draw += 1

print(f'У Славы {money_one_player}. У Папы {money_two_player}')

print(f'Слава выиграл {score_one} раз')
print(f'Папа выиграл {score_two} раз')
print(f'Ничья {score_draw} раз')

param = {
    'table_cards': table,
    'first_player_cards': one_player,
    'second_player_cards': two_player,
    'result': winner
}

return render_template('index.html', **param)