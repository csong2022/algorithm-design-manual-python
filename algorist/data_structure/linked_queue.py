class Node:
    def __init__(self, item, next=None):
        self.item = item  # data item
        self.next = next  # point to successor


class QueueIterator:
    def __init__(self, first: Node):
        self.current = first

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            x = self.current.item
            self.current = self.current.next
            return x


class Queue:
    """
    Implementation of a FIFO queue abstract data type.
    """

    def __init__(self):
        self.count = 0  # number of queue elements
        self.first = None  # first element
        self.last = None  # last element

    def enqueue(self, x) -> None:
        old_last = self.last
        self.last = Node(x)
        if self.is_empty():
            self.first = self.last
        else:
            old_last.next = self.last
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError('Queue underflow')
        else:
            x = self.first.item
            self.first = self.first.next
            self.count -= 1
            if self.is_empty():
                self.last = None
            return x

    def headq(self):
        if self.is_empty():
            raise IndexError('Queue empty')
        else:
            return self.first.item

    def is_empty(self) -> bool:
        return self.count == 0

    def __iter__(self):
        return QueueIterator(self.first)

    def print(self) -> None:
        print(' '.join(str(x) for x in self))
