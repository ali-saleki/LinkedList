# This is a sample Python script.

# Hi this is my python script for linked lists.


class Node: #in some functions we need to create a node so we create a seperate class.
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def print_list(self): # display the list
        temp = self.head
        print('the list is [', end='')
        while temp is not None:
            if temp != self.head:
                print(',', end='')
            print(temp.value, end='')
            temp = temp.next
        print(']')
    def append(self, value): #append method
        new_node = Node(value)
        if self.head is None: # when list is empty
            self.head = new_node
            self.tail = new_node
            self.length += 1
            self.tail.next = None
            return True
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        return True
    def pop(self): #pop method
        if self.head is None:
            return False
        temp = self.head
        while temp.next is not None:
            prev = temp
            temp = temp.next
        self.tail = prev
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return True
    def prepend(self, value): # add value in the first place.
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.tail.next = None
            return True
        temp = self.head
        self.head = new_node
        self.head.next = temp
        self.length += 1
        return True
    def pop_first(self): # remove the first item in the list.
        if self.length == 0: # check if list is empty
            return False
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return True
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    def set_value(self, index, value):
        temp = self.get(index)
        if temp: #check if temp is not None
            temp.value = value
            return True
        return False
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    def remove(self, index):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index + 1)
        prev = self.get(index - 1)
        prev.next = temp
        self.length -= 1
        return True
    def reverse(self):
        if self.length == 0:
            return False
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return True