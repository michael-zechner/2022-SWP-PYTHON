'''
0 .... Pic
1 .... Kreuz
2 .... Karo
3 .... Herz
-----------
1  .... Ass
11 .... Bube
12 .... Dame
13 .... König
'''

class Card:
    def __init__(self, color, symbol):
        self.color = color
        self.symbol = symbol

    def __str__(self):
        back = str(self.color) + "/" + str(self.symbol)
        return back