#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Implementation of a LIFO stack abstract data type.

Translate from stack.h, stack.c. Add iterator implementation.
*"""

__author__ = "csong2022"


class Node:
    def __init__(self, item, _next=None):
        self.item = item  # data item
        self.next = _next  # point to successor


class StackIterator:
    def __init__(self, first: Node):
        self.current = first

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            x = self.current.item
            self.current = self.current.next
            return x


class Stack:
    """
    Implementation of a LIFO stack abstract data type.
    """

    def __init__(self):
        self.first = None  # top of stack
        self.n = 0  # number of stack elements

    def push(self, x) -> None:
        self.first = Node(x, self.first)
        self.n += 1

    def pop(self):
        if self.is_empty():
            raise IndexError('Stack underflow')
        else:
            x = self.first.item
            self.first = self.first.next
            self.n -= 1
            return x

    def is_empty(self) -> bool:
        return self.n == 0

    def __iter__(self):
        return StackIterator(self.first)

    def print(self) -> None:
        for x in self:
            print(x, end=' '),
        print()
