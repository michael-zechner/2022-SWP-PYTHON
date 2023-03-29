from random import randint


class DoubleLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, object):
        newNode = Node(object)
        if self.head == None:
            self.head = self.tail = newNode 
            self.head.previous = None
            self.tail.next = None
        else:
            self.tail.next = newNode
            newNode.previous = self.tail
            self.tail = newNode
            self.tail.next = None
            
    def prepend(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
    def clear(self):
        self.head = None
        self.tail = None

    def copy(self):
        new_list = DoubleLinkedList()
        current = self.head
        while current is not None:
            new_node = Node(current.obj[0])
            if new_list.head is None:
                new_list.head = new_node
                new_list.tail = new_node
            else:
                new_node.prev = new_list.tail
                new_list.tail.next = new_node
                new_list.tail = new_node
            current = current.next
        return new_list

    def count(self, data):
        count = 0
        current = self.head
        while current is not None:
            if current.obj[0] == data:
                count += 1
            current = current.next
        return count

    def extend(self, data):
        for element in data:
            self.append(element)

    def get_index(self, data):
        current_node = self.head
        index = 0
        while current_node:
            if current_node.obj[0] == data:
                return index
            current_node = current_node.next
            index += 1
        raise ValueError

    def insert(self, index, data):
        if index < 0 or index > self.length():
            raise IndexError("Index out of range")
        if index == 0:
            self.prepend(data)
        elif index == self.length():
            self.append(data)
        else:
            new_node = Node(data)
            current_node = self.head
            for i in range(index-1):
                current_node = current_node.next
            new_node.next = current_node.next
            new_node.prev = current_node
            current_node.next.prev = new_node
            current_node.next = new_node

    def pop(self, index=-1):
        if self.length() == 0:
            raise Exception("Cannot pop from empty list")
        if index < 0:
            index += self.length()
        if index < 0 or index >= self.length():
            raise IndexError("Index out of range")
        curr = self.head
        for i in range(index):
            curr = curr.next
        if curr == self.head:
            self.head = curr.next
            self.head.prev = None
        elif curr == self.tail:
            self.tail = curr.prev
            self.tail.next = None
        else:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
        return curr.obj

    def remove(self, data):
        current_node = self.head
        while current_node:
            if current_node.obj[0] == data:
                if current_node.prev is None:
                    self.head = current_node.next
                    current_node.next.prev = None
                elif current_node.next is None:
                    self.tail = current_node.prev
                    current_node.prev.next = None
                else:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                return
            current_node = current_node.next
        raise ValueError("Data not found in list")

    def reverse(self):
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = current_node.previous
            current_node.previous = next_node
            if not next_node:
                self.head = current_node
            current_node = next_node

    def sort(self):
        current = self.head
        if current is None:
            return
        while current.next is not None:
            index = current.next
            while index is not None:
                if current.obj > index.obj:
                    temp = current.obj
                    current.obj = index.obj
                    index.obj = temp
                index = index.next
            current = current.next
    # End Methods from W3Schools

    def length(self):
        count = 0
        curr = self.head
        while curr is not None:
            count += 1
            curr = curr.next
        return count

    def print_list(self):
        current = self.head;    
        if(self.head == None):    
            print("List is empty");    
            return;    
        print("Nodes of doubly linked list: ");    
        while(current != None):     
            print(current.obj[0]),;    
            current = current.next;  

    def max(self):
        if self.head is None:
            return None
        else:
            max_val = self.head.obj
            curr = self.head.next
            while curr is not None:
                if curr.obj > max_val:
                    max_val = curr.obj
                curr = curr.next
            return max_val[0]
    
    def min(self):
        if self.head is None:
            return None
        else:
            min_val = self.head.obj
            curr = self.head.next
            while curr is not None:
                if curr.obj < min_val:
                    min_val = curr.obj
                curr = curr.next
            return min_val[0]

    def contains_element(self,object):
        curr = self.head
        while curr is not None:
            if curr.obj[0] == object:
                return True
            curr = curr.next
        return False

    def sum(self):
        curr = self.head
        total = 0
        while curr is not None:
            total += curr.obj[0]
            curr = curr.next
        return total
    
    def get_first_element(self):
        return self.head.obj[0]

    def get_last_element(self):
        return self.tail.obj[0]


        
class Node():
    def __init__(self, object):
        self.obj = int(object),
        self.next = None
        self.previous = None
    
    def __repr__(self):
        return str(self.obj[0])

def fill_with_numbers(l,how_many,stop):
    for i in range(how_many):
        l.append(randint(1,stop))

if __name__ == '__main__':
    l = DoubleLinkedList()
    l.append(5)
    l.append(7)
    l.insert(0,3)
    l.print_list()
    l.reverse()
    l.print_list()


    # def remove_at(self, index):
    #     if index < 0 or index >= self.length():
    #         raise IndexError("Index out of range")
    #     current_node = self.head
    #     if index == 0:
    #         self.head = current_node.next
    #         current_node.next.prev = None
    #     elif index == self.length()() - 1:
    #         self.tail = self.tail.prev
    #         self.tail.next = None
    #     else:
    #         for i in range(index):
    #             current_node = current_node.next
    #         current_node.prev.next = current_node.next
    #         current_node.next.prev = current_node.prev