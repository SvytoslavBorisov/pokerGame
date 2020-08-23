from card import Card
from const import suits, numbers
import random


class Deck:

    def __init__(self, count=52):

        self.cards = []

        for siut in suits.values():
            for number in numbers:
                card = Card(suit=siut, number=number)
                self.cards.append(card)

    def get_all_cards(self):
        return [str(card) for card in self.cards]

    def get_cards_player(self, count=2):

        player_cards = []
        random.shuffle(self.cards)

        for i in range(len(self.cards)):
            if self.cards[i].activity and len(player_cards) < count:
                self.cards[i].activity = False
                player_cards.append(self.cards[i])
            if len(player_cards) >= count:
                return player_cards
        return 'error'

    def new_game(self):
        for i in range(len(self.cards)):
            self.cards[i].activity = True
