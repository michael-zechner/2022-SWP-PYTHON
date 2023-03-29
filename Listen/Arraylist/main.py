class Arraylist():
    def __init__(self):
        self.element = []

    def append(self, object):
        self.element.append(object) 

    def clear(self):
        self.element.clear()

    def copy(self):
        return self.element.copy()

    def count(self, data):
        return self.element.count(data)

    def extend(self, data):
        self.element.extend(data)

    def get_index(self, data):
        return self.element.index(data)

    def insert(self, index, data):
        self.element.insert(index,data)

    def pop(self, index):
        self.element.pop(index)

    def remove(self, data):
        self.element.remove(data)
        
    def reverse(self):
        return self.element.reverse()

    def sort(self):
        self.element.sort()
    # End Methods from W3Schools

    def length(self):
        return len(self.element)

    def print_list(self):
        print(self.element)

    def max(self):
        return max(self.element)
    
    def min(self):
        return min(self.element)

    def contains_element(self,object):
        return self.element.__contains__(object)

    def sum(self):
        return sum(self.element)
    
    def get_first_element(self):
        return self.element[0]

    def get_last_element(self):
        return self.element[::1]

if __name__ == '__main__':
    a = Arraylist()