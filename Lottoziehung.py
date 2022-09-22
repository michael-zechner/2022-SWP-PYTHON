import random

def init(x):
    selection = []
    for i in range(1,x+1):
        selection.append(i)
        dict[i] = 0
    return selection

dict = {}
selection = init(45)

def randomizer():
    i = 1
    while i < 7:
        value = random.randint(0,len(selection)-1)
        selection[value], selection[len(selection)-i] = selection[len(selection)-i], selection[value]
        dict[value+1] += 1
        i = i + 1

if __name__ == "__main__":
    cnt = 1
    while cnt < 1000:
        randomizer()
        cnt = cnt + 1
    print(dict)