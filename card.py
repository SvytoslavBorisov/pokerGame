from const import suits


class Card:

    def __init__(self, suit='heart', number='2'):
        self.suit = suits[suit]
        self.number = number
        self.activity = True

    def __repr__(self) -> str:
        return self.suit + ' ' + self.number

    def __str__(self) -> str:
        return self.suit + ' ' + self.number

    def __int__(self) -> int:
        if self.number == 'jack':
            return 11
        elif self.number == 'queen':
            return 12
        elif self.number == 'king':
            return 13
        elif self.number == 'ace':
            return 14
        else:
            return int(self.number)

    def __gt__(self, other) -> bool:
        print(self, other)
        if int(self) > int(other):
            return True
        elif int(self) < int(other):
            return False
        else:
            return False

    def __lt__(self, other) -> bool:

        if self.__int__() > other.__int__():
            return False
        elif int(self) < int(other):
            return True
        else:
            return False
