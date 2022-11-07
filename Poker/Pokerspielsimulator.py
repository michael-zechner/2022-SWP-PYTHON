from random import randrange
from model import Card
from collections import Counter
from copy import deepcopy
import numpy as np

def init():
    for i in range(0,4):
        for j in range(1,14):
            c = Card(i,j)
            cards.append(c)

def getRandCards():
    draw_cards.clear()
    draw_color.clear()
    draw_symbol.clear()
    length = len(cards)-1
    for i in range(5):
        index = randrange(length-i)
        value = cards[index]
        draw_cards.append(value)
        draw_color.append(value.color)
        draw_symbol.append(value.symbol)
        cards[index], cards[length-i] = cards[length-i], value

def highestCard():
    value = 0
    highest_card = max(draw_cards, key=lambda x:x.symbol)
    value = highest_card
    lowest_card = min(draw_cards, key=lambda x:x.symbol)
    if lowest_card.symbol == 1:
        value = lowest_card
    return True

def pair():
    counts = dict(Counter(draw_symbol))
    duplicates = {key:value for key, value in counts.items() if value > 1}
    if len(duplicates) == 1:
        return True
    return False

def twoPairs():
    counts = dict(Counter(draw_symbol))
    duplicates = {key:value for key, value in counts.items() if value > 1}
    if len(duplicates) == 2:
        return True
    return False

def drilling():
    counts = dict(Counter(draw_symbol))
    duplicates = {key:value for key, value in counts.items() if value > 2}
    if len(duplicates) == 1:
        return True
    return False

def straight():
    symbols = deepcopy(draw_symbol)
    symbols.sort()
    if symbols[4] == 13:
        if symbols[0] == 1:
            symbols.remove(1)
    if symbols == list(range(min(symbols), max(symbols)+1)):
        return True
    else:
       return False

def flush():
    counts = dict(Counter(draw_color))
    duplicates = {key:value for key, value in counts.items() if value > 4}
    if len(duplicates) == 1:
        return True
    return False

def fullHouse():
    if twoPairs() and drilling():
            return True
    return False

def fourofakind():
    counts = dict(Counter(draw_symbol))
    four = {key:value for key, value in counts.items() if value > 3} 
    if len(four) > 0:
        return True
    else: 
        return False

def straightFlush():
    if flush():
        if straight():
            return True
    return False

def royaleFlush():
    symbols = deepcopy(draw_symbol)
    symbols.sort()
    if symbols[0] == 1:
        symbols.remove(1)
        symbols.append(1)
    if flush():
        if symbols [0] == 10:
            if symbols [1] == 11:
                if symbols [2] == 12:
                    if symbols [3] == 13:
                        if symbols[4] == 1:
                            return True
    return False

def valuation():
    if royaleFlush():
        stats["royal Flush"] += 1
    elif straightFlush():
        stats["straight Flush"] += 1
    elif fourofakind():
        stats["four of a kind"] += 1
    elif fullHouse():
        stats["full House"] += 1
    elif flush():
        stats["Flush"] += 1
    elif straight():
        stats["Straight"] += 1
    elif drilling():
        stats["Drilling"] += 1
    elif twoPairs():
        stats["two Pairs"] += 1
    elif pair():
        stats["Pair"] += 1
    elif highestCard():
        stats["highest Card"] += 1

if __name__ == "__main__":
    howoften = 1000000
    cards = []
    draw_cards = []
    draw_color = []
    draw_symbol = []
    stats = {
        "highest Card" : 0.0,
        "Pair" : 0.0,
        "two Pairs" : 0.0,
        "Drilling" : 0.0,
        "Straight" : 0.0,
        "Flush" : 0.0,
        "full House" : 0.0,
        "four of a kind" : 0.0,
        "straight Flush" : 0.0,
        "royal Flush" : 0.0,
    }
    init()
    for i in range(howoften):
        getRandCards()
        valuation()
    print('Stat:')
    stats = {key: (value / howoften)*100 for key, value in stats.items()}
    print(stats)