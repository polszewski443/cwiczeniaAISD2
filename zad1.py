class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, value):
        newnode = Node(value)
        newnode.next = self.head
        self.head = newnode
        self.length += 1

    def append(self, value):
        newnode = Node(value)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newnode
        else:
            self.head = newnode
        self.length += 1

    def node(self, index):
        if index >= self.length:
            return
        if self.head is None:
            return
        current = self.head
        howmany = 0
        while howmany != index:
            howmany += 1
            current = current.next
        return current.value

    def insert(self, after, value):
        newnode = Node(value)

        if self.head is None:
            self.head = newnode
        else:
            current = self.head
            count = 1
            while current is not None and count < after:
                current = current.next
                count += 1
            newnode.next = current.next
            current.next = newnode
        self.length += 1

    def pop(self):
        current = self.head
        if self.head is not None:
            self.head = self.head.next
            self.length -= 1
        return current.value

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
        self.length -= 1
        return current.value

    def remove(self, index):
        if self.head is None:
            return
        current = self.head
        if (index+1) == 0:
            self.head = current.next
            current = None
            return
        for i in range(index):
            current = current.next
            if current is None:
                break
        if current is None:
            return
        if current.next is None:
            return
        next = current.next.next
        current.next = None
        current.next = next
        self.length -= 1

    def print(self):
        current = self.head
        while current is not None:
            print(current.value, "->", end=" ")
            current = current.next
        print("None")

    def len(self):
        return self.length


class Stack:
    _storage: LinkedList

    def __init__(self):
        self.element = []

    def push(self, value):
        self._storage.push(value)

    def pop(self):
        self._storage.pop()

    def print(self):
        self._storage.print()

    def len(self):
        self._storage.len()


stack = Stack()
stack.push(3)
stack.push(10)
stack.print()
