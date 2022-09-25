import random

def init(x):
    selection = []
    for i in range(1,x+1):
        selection.append(i)
        dict[i] = 0
    return selection

dict = {}
selection = init(45)

def statistik(value):
    dict[value+1] += 1

def randomizer():
    i = 1
    while i < 7:
        value = random.randint(1,len(selection)-i)
        selection[value], selection[len(selection)-i] = selection[len(selection)-i], selection[value]
        statistik(value)
        i = i + 1

if __name__ == "__main__":
    cnt = 1
    while cnt < 1000:
        randomizer()
        cnt = cnt + 1
    print(dict)