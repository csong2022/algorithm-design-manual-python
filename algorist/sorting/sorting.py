#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Sorting algorithms.

Translate from sorting.c.
"""

__author__ = "csong2022"

from algorist.data_structure.priority_queue import PriorityQueue


def swap(s: list, i: int, j: int) -> None:
    if i != j:
        s[i], s[j] = s[j], s[i]


def less(a, b, key=None):
    if key is None:
        return a < b
    else:
        return key(a) < key(b)


def insertion_sort(s: list, n: int, key=None) -> None:
    """Insertion sort."""
    for i in range(1, n):
        j = i
        while j > 0 and less(s[j], s[j - 1], key):
            swap(s, j, j - 1)
            j -= 1


def selection_sort(s: list, n: int, key=None) -> None:
    """Selection sort."""
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if less(s[j], s[min_index], key):
                min_index = j
        swap(s, i, min_index)


def quicksort(s: list, l: int, h: int, key=None) -> None:
    """Quick sort."""
    if h > l:
        p = partition(s, l, h, key)
        quicksort(s, l, p - 1, key)
        quicksort(s, p + 1, h, key)


def partition(s: list, l: int, h: int, key=None) -> int:
    p = h
    first_high = l
    for i in range(l, h):
        if less(s[i], s[p], key):
            swap(s, i, first_high)
            first_high += 1
    swap(s, p, first_high)

    return first_high


def heapsort(s: list, n: int, key=None) -> None:
    """Heap sort."""
    q = PriorityQueue.make_heap(s, n, key)  # heap for heapsort

    for i in range(0, n):
        s[i] = q.extract_min()


def binary_search(s: list, val, low: int, high: int, key=None) -> int:
    """Binary search."""
    if low > high:  # key not found
        return -1

    middle = (low + high) // 2  # index of middle element, this is integer divide
    if less(val, s[middle], key):
        return binary_search(s, val, low, middle - 1)
    elif less(s[middle], val, key):
        return binary_search(s, val, middle + 1, high)
    else:
        return middle


def mergesort(s: list, low: int, high: int, key=None) -> None:
    """Merge sort."""
    if low < high:
        aux = s[:]
        _mergesort(s, aux, low, high, key)


def _mergesort(s: list, aux: list, low: int, high: int, key=None) -> None:
    if low < high:
        middle = (low + high) // 2  # index of middle element, this is integer divide
        _mergesort(s, aux, low, middle, key)
        _mergesort(s, aux, middle + 1, high, key)

        _merge(s, aux, low, middle, high, key)


def _merge(s: list, aux: list, low: int, middle: int, high: int, key=None) -> None:
    aux[low:high + 1] = s[low:high + 1]

    i = low
    j = middle + 1

    for k in range(low, high + 1):
        if i > middle:
            s[k] = aux[j]
            j += 1
        elif j > high:
            s[k] = aux[i]
            i += 1
        elif less(aux[i], aux[j], key):
            s[k] = aux[i]
            i += 1
        else:
            s[k] = aux[j]
            j += 1


def is_sorted(s: list, key=None) -> bool:
    """Test if list is sorted?"""
    return all(not less(s[i + 1], s[i], key) for i in range(len(s) - 1))
