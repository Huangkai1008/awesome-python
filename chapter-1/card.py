"""
有序的纸牌
"""
import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    """
    扑克牌
    """
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')  # 点数
    suits = 'spades diamonds clubs hearts'.split()  # 花色

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


deck = FrenchDeck()

length = len(deck)

print(choice(deck))
