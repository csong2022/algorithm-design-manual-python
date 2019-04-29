#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Binary search tree container implementation.

Translate from tree.h, tree-demo.c.
"""

__author__ = "csong2022"


class Node:
    """Tree node."""

    def __init__(self, item, parent):
        self.item = item  # data item
        self.parent = parent  # pointer to parent
        self.left = None  # pointer to left child
        self.right = None  # pointer to right child


class Tree:

    def __init__(self):
        self.root = None

    def is_empty(self) -> bool:
        """Is tree empty?"""
        return self.root is None

    def __contains__(self, x):
        """Does tree contains value?"""
        return self._search(self.root, x) is not None

    def _search(self, l: Node, x) -> Node:
        if l is None:
            return None

        if x == l.item:
            return l
        elif x < l.item:
            return self._search(l.left, x)
        else:
            return self._search(l.right, x)

    def insert(self, x) -> None:
        """Insert value to the tree."""
        self.root = self._insert(self.root, x)

    def _insert(self, l: Node, x, parent: Node = None) -> Node:
        if l is None:
            return Node(x, parent)

        if x < l.item:
            l.left = self._insert(l.left, x, l)
        elif x > l.item:
            l.right = self._insert(l.right, x, l)
        return l

    def print(self) -> None:
        self._print(self.root)

    def _print(self, l) -> None:
        if l is not None:
            self._print(l.left)
            print("%s " % l.item, end='')
            self._print(l.right)

    def _successor_descendant(self, t: Node) -> Node:
        if t.right is None:
            return None

        succ = t.right
        while succ.left is not None:
            succ = succ.left

        return succ

    def _find_minimum(self, t: Node) -> Node:
        if t is None:
            return None

        _min = t
        while _min.left is not None:
            _min = _min.left
        return _min

    def _predecessor_descendant(self, t: Node) -> Node:
        if t.left is None:
            return None

        pred = t.left
        while pred.right is not None:
            pred = pred.right

        return pred

    def delete(self, x):
        """Delete value."""
        self.root = self._delete(self.root, x)

    def _delete(self, t: Node, x) -> Node:
        d = self._search(t, x)

        if d is None:
            print("Warning: key to be deleted %s is not in tree." % x)
            return t

        if d.parent is None:  # if d is the root
            if d.left is None and d.right is None:
                return None  # root-only tree

            if d.left is not None:  # find node to physically delete
                p = self._predecessor_descendant(d)
            else:
                p = self._successor_descendant(d)
        else:
            if d.left is None or d.right is None:
                # d has <=1 child, so try to find non-null child
                if d.left is not None:
                    child = d.left
                else:
                    child = d.right

                if d.parent.left == d:  # fill null pointer
                    d.parent.left = child
                else:
                    d.parent.right = child

                if child is not None:
                    child.parent = d.parent
                return t
            else:  # p has 2 children
                p = self._successor_descendant(d)

        new_key = p.item  # deal with simpler case of deletion
        self._delete(t, p.item)
        d.item = new_key
        return t
