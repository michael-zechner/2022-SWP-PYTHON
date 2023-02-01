from random import randint

'''
The begining zero is equal to 'head'

Folgende Anforderungen sind gegeben:
- Datenstruktur als Objekt instanzierbar            (✓)
- Ganzahl-werte als Werte der Datenstruktur         (✓) 
- programmiere Methode "am Ende Hinzufügen"         (✓) (append)
- programmiere Ausgabe Länge der Datenstruktur      (✓)
- Ausgabe aller Elemente                            (✓) 
- main mit exemplarischen (Zufallszahlen) Befüllen  (✓)

Extra:
- List Methods from W3School (10 + append)
    [clear,copy,count,extend,get_index,insert,pop,remove,reverse,sort]
- max
- min
- sum
- contains (boolean)
- last element
- first element
'''

class LinkedList():
    def __init__(self):
        self.start_element = ListElement(0)

    def append(self,object):
        new_element = ListElement(object)
        last_element = self.get_last_element()
        last_element.next_element = new_element

    def clear(self):
        le = self.start_element
        le.next_element = None

    def copy(self):
        l = LinkedList()
        le_new = l.start_element
        le = self.start_element
        while le.next_element is not None:
            le_new.next_element = le.next_element
            le_new = le_new.next_element
            le = le.next_element
        return l

    def count(self, object):
        cnt = 0
        le = self.start_element
        while le is not None:
            if le.obj[0] == object:
                cnt += 1
            le = le.next_element
        return cnt

    def extend(self, object):
        last_element = self.get_last_element()
        for i in object:
            if last_element.next_element is None:
                last_element.next_element = ListElement(i)
            last_element = last_element.next_element

    def get_index(self,object):
        index = 0
        le = self.start_element
        while le is not None:
            if le.obj[0] == object:
                return index
            index += 1
            le = le.next_element

    def insert(self, index, new_item):
        pointer_element = self.start_element
        while pointer_element is not None and not self.get_index(pointer_element.obj[0]) == index:
            pointer_element = pointer_element.next_element
        new_element = ListElement(new_item)
        next_element = pointer_element.next_element
        pointer_element.next_element = new_element
        new_element.next_element = next_element

    def pop(self,index):
        le = self.start_element
        while le.next_element is not None:
            if self.get_index(le.obj[0]) == index:
                le.next_element = le.next_element.next_element
            le = le.next_element

    def remove(self,object):
        le = self.start_element
        while (le.next_element is not None) and not (le.obj[0] == object):
            if le.next_element.obj[0] == object:
                if le.next_element.next_element is not None:
                    le.next_element = le.next_element.next_element
                else:
                    le.next_element = None
                    break
            le = le.next_element

    def reverse(self):
        previous = None
        le = self.start_element
        while le is not None:
            next_element = le.next_element
            le.next_element = previous
            previous = le
            le = next_element
        self.start_element = previous

    def sort(self):
        le = self.start_element
        index = None
        while le is not None:
            index = le.next_element
            while index is not None:
                if le.obj[0] > index.obj[0]:
                    temp = le.obj
                    le.obj = index.obj
                    index.obj = temp
                index = index.next_element
            le = le.next_element
    # End Methods from W3Schools

    def length(self):
        len = 0
        le = self.start_element
        while le is not None:
            len += 1
            le = le.next_element
        return len

    def print_list(self):
        le = self.start_element
        while le is not None:
            print(le)
            le = le.next_element
    # End Instruction

    def max(self):
        max = 0
        le = self.start_element
        while le is not None:
            if max < le.obj[0]:
                max = le.obj[0]
            le = le.next_element
        return max
    
    def min(self):
        min = self.start_element.next_element.obj[0] 
        le = self.start_element.next_element
        while le is not None:
            if le.obj[0] < min:
                min = le.obj[0]
            le = le.next_element
        return min

    def contains_element(self,object):
        le = self.start_element
        while le is not None:
            if le.obj[0] == object:
                return True
            le = le.next_element
        return False

    def sum(self):
        cnt = 0
        le = self.start_element
        while le is not None:
            cnt += le.obj[0]
            le = le .next_element
        return cnt
    
    def get_first_element(self):
        return self.start_element

    def get_last_element(self):
        le = self.start_element
        while le.next_element is not None:
            le = le.next_element
        return le


        
class ListElement():
    def __init__(self, object):
        self.obj = int(object),
        self.next_element = None
    
    def __repr__(self):
        return str(self.obj[0])

def fill_with_numbers(l,how_many,start,stop):
    for i in range(how_many):
        l.append(randint(start,stop))

if __name__ == '__main__':
    l = LinkedList()
    fill_with_numbers(l,5,0,50)
    l.print_list()
    print('------------')