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
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode

    def append(self, value):
        newNode = Node(value)
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def show(self):
        current = self.head
        while (current):
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

    def remove(self, after: Node):

list = LinkedList()
list.append(3)
list.append(4)
list.push(1)
list.push(2)
list.append(5)
list.show()
list.remove_last()
list.show()


