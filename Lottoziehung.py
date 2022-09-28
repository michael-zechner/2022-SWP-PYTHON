import random

def init(start,stop):
    selection = []
    for i in range(start,stop+1):
        selection.append(i)
        dict[i] = 0
    return selection

def statistik(value):
    dict[value+1] += 1

def randomizer(cnt):
    i = 1
    while i <= cnt:
        value = random.randint(0,len(selection)-i)
        selection[value], selection[len(selection)-i] = selection[len(selection)-i], selection[value]
        statistik(value)
        i = i + 1

if __name__ == "__main__":
    dict = {}
    selection = []
    selection = init(1,45)
    for i in range(1000):
        randomizer(6)
    print(dict)