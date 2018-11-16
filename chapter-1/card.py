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


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    """
    扑克牌排序
    :param card:
    :return:
    """
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


deck = FrenchDeck()

length = len(deck)

print(choice(deck))


for card in sorted(deck, key=spades_high):
    print(card)
