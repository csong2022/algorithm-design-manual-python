#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Implementation of a heap / priority queue abstract data type.

Translate from priority_queue.h, priority_queue.c.
"""

__author__ = "csong2022"


class PriorityQueue:

    def __init__(self):
        self.q = [None]  # body of queue
        self.n = 0  # number of queue elements

    def _parent(self, n: int) -> int:
        """parent index."""
        return -1 if n == 1 else int(n / 2)

    def _young_child(self, n: int) -> int:
        """Index of younger children."""
        return 2 * n

    def bubble_up(self, p: int) -> None:
        """Bubble up o ensure the heap order."""
        parent = self._parent(p)
        if parent == -1:  # at root of heap, no parent
            return

        if self.q[parent] > self.q[p]:
            self.swap(p, parent)
            self.bubble_up(parent)

    def bubble_down(self, p: int) -> None:
        """Bubble down o ensure the heap order."""
        c = self._young_child(p)  # child index
        min_index = p

        for i in range(2):
            if c + i <= self.n:
                if self.q[min_index] > self.q[c + i]:
                    min_index = c + i

        if min_index != p:
            self.swap(p, min_index)
            self.bubble_down(min_index)

    def insert(self, x) -> None:
        """Insert value"""
        self.q.append(x)
        self.n += 1
        self.bubble_up(self.n)

    def extract_min(self):
        """Remove the minimum value from priority queue."""
        _min = None  # minimum value

        if self.is_empty():
            print("Warning: empty priority queue.")
        else:
            _min = self.q[1]

            self.q[1] = self.q[self.n]
            self.q[self.n] = None
            self.n -= 1
            self.bubble_down(1)

        return _min

    def is_empty(self) -> bool:
        """Is priority queue empty?"""
        return self.n == 0

    def swap(self, i, j) -> None:
        if i != j:
            self.q[i], self.q[j] = self.q[j], self.q[i]

    def print(self) -> None:
        print(self.q[1: self.n], end=' ')

    def __len__(self):
        return self.n

    @staticmethod
    def make_heap(s: list, n: int):
        """Construct heap from list"""
        q = PriorityQueue()

        for i in range(0, n):
            q.q.append(s[i])

        q.n = n

        for i in range(n, 0, -1):
            q.bubble_down(i)

        return q

    @staticmethod
    def make_heap1(s: list, n: int):
        """Construct heap from list"""
        q = PriorityQueue()

        for i in range(0, n):
            q.insert(s[i])

        return q
