#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Implementation of a FIFO queue abstract data type.

Translate from queue.h, queue.c. Implement with singly linked list. Add iterator implementation.
"""

__author__ = "csong2022"


class Node:
    """Queue node."""

    def __init__(self, item, _next=None):
        self.item = item  # data item
        self.next = _next  # point to successor


class Queue:
    def __init__(self):
        self.count = 0  # number of queue elements
        self.first = None  # first element
        self.last = None  # last element

    def enqueue(self, x) -> None:
        """Enqueue"""
        old_last = self.last
        self.last = Node(x)
        if self.is_empty():
            self.first = self.last
        else:
            old_last.next = self.last
        self.count += 1

    def dequeue(self):
        """Dequeue"""
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
        """Head of the queue."""
        if self.is_empty():
            raise IndexError('Queue empty')
        else:
            return self.first.item

    def is_empty(self) -> bool:
        """Is queue empty?"""
        return self.count == 0

    def __iter__(self):
        """Iterate through the queue in FIFO sequence."""
        current = self.first
        while current is not None:
            yield current.item
            current = current.next

    def print(self) -> None:
        print(' '.join(str(x) for x in self))

    def size(self):
        return self.count
