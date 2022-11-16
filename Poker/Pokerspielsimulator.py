from random import randrange
from model import Card
from collections import Counter
from copy import deepcopy

def init():
    cards = []
    for i in range(0,4):
        for j in range(1,14):
            c = Card(i,j)
            cards.append(c)
    return cards

def getRandCards(cnt):
    draw_cards = []
    draw_color = []
    draw_symbol = []
    length = len(cards)-1
    for i in range(cnt):
        index = randrange(length-i)
        value = cards[index]
        draw_cards.append(value)
        draw_color.append(value.color)
        draw_symbol.append(value.symbol)
        cards[index], cards[length-i] = cards[length-i], value
    return draw_cards, draw_color, draw_symbol    

def highestCard():
    value = 0
    highest_card = max(draw_symbol)
    value = highest_card
    lowest_card = min(draw_symbol)
    if lowest_card == 1:
        value = lowest_card
    return True

def pair():
    counts = dict(Counter(draw_symbol))
    duplicates = {key:value for key, value in counts.items() if value == 2}
    if len(duplicates) == 1:
        return True
    return False

def twoPairs():
    counts = dict(Counter(draw_symbol))
    duplicates = {key:value for key, value in counts.items() if value == 2}
    if len(duplicates) == 2:
        return True
    return False

def drilling():
    counts = dict(Counter(draw_symbol))
    duplicates = {key:value for key, value in counts.items() if value == 3}
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
    duplicates = {key:value for key, value in counts.items() if value == 5}
    if len(duplicates) == 1:
        return True
    return False

def fullHouse():
    if drilling() and pair():
            return True
    return False

def fourofakind():
    counts = dict(Counter(draw_symbol))
    four = {key:value for key, value in counts.items() if value == 4} 
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
        stats["Royal-Flush"] += 1
    elif straightFlush():
        stats["Straight-Flush"] += 1
    elif fourofakind():
        stats["Four-of-a-Kind"] += 1
    elif fullHouse():
        stats["Full-House"] += 1
    elif flush():
        stats["Flush"] += 1
    elif straight():
        stats["Straight"] += 1
    elif drilling():
        stats["Drilling"] += 1
    elif twoPairs():
        stats["Two-Pairs"] += 1
    elif pair():
        stats["Pair"] += 1
    elif highestCard():
        stats["Highest-Card"] += 1

if __name__ == "__main__":
    howoften = int(input("Wie oft soll gezogen werden? "))
    howmanycards = int(input("Wie viel Karten sollen gezogen werden? "))
    stats = {
        "Highest-Card" : 0.0,
        "Pair" : 0.0,
        "Two-Pairs" : 0.0,
        "Drilling" : 0.0,
        "Straight" : 0.0,
        "Flush" : 0.0,
        "Full-House" : 0.0,
        "Four-of-a-Kind" : 0.0,
        "Straight-Flush" : 0.0,
        "Royal-Flush" : 0.0,
    }
    cards = init()
    for i in range(howoften):
        draw_cards, draw_color, draw_symbol = getRandCards(howmanycards)
        valuation()
    file = open("Poker/wikipedia.txt", "r")
    data = list(map(float, file.read().split("\n")))
    file.close()
    print('')
    print("Gezogene Karten: " + str(howmanycards))
    print("Wie viel Ziehungen: " + str(howoften))
    print('-------------------------------------')
    print('Statistik:')
    print('')
    print("{:<15} {:<20} {:<12} {:<10}".format('Kombination', 'Wahrscheinlichkeit', 'Wikipedia', 'Abweichung'))
    stats = {key: round((value / howoften)*100,4) for key, value in stats.items()}
    cnt = 0
    for key, value in stats.items():
        diff = round(abs(data[cnt] - value),4)
        print("{:<15} {:<7}% {:<11} {:<8}% {:<2} {:<7}%".format(key,value,"",data[cnt],"", diff))
        cnt+=1