from typing import Any


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value):
        newnode = Node(value)
        newnode.next = self.head
        self.head = newnode

    def append(self, value):
        newnode = Node(value)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newnode
        else:
            self.head = newnode

    def node(self, at):
        if self.head is None:
            return
        current = self.head
        howmany = 0
        while howmany != at:
            howmany += 1
            current = current.next
        return current.value

    def insert(self, value, after):
        if self.head is None:
            return
        current = self.head
        howmany = 0
        while howmany != after:
            howmany += 1
            current = current.next
        newnode = Node(value)
        newnode.next = current
        current = newnode


    def show(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def remove_last(self):
        if self.head is None:
            return None
        previous = None
        current = self.head
        while current.next is not None:
            previous = current
            current = current.next
        if previous:
            previous.next = None
        return current


list = LinkedList()
list.append(3)
list.append(4)
list.push(1)
list.push(6)
list.append(5)
list.show()
print("")
list.remove_last()
list.show()
print("")
print(list.node(0))
