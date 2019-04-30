#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Binary search tree container implementation.

Translate from tree.h, tree-demo.c.
"""

__author__ = "csong2022"


def less(a, b, key=None):
    if key is None:
        return a < b
    else:
        return key(a) < key(b)


class Node:
    """Tree node."""

    def __init__(self, item, parent):
        self.item = item  # data item
        self.parent = parent  # pointer to parent
        self.left = None  # pointer to left child
        self.right = None  # pointer to right child


class Tree:

    def __init__(self, key=None):
        self.root = None
        self.key = key

    def is_empty(self) -> bool:
        """Is tree empty?"""
        return self.root is None

    def __contains__(self, x):
        """Does tree contains value?"""
        return self._search(self.root, x) is not None

    def _search(self, l: Node, x) -> Node:
        if l is None:
            return None

        if less(x, l.item, self.key):
            return self._search(l.left, x)
        elif less(l.item, x, self.key):
            return self._search(l.right, x)
        else:
            return l

    def insert(self, x) -> None:
        """Insert value to the tree."""
        self.root = self._insert(self.root, x)

    def _insert(self, l: Node, x, parent: Node = None) -> Node:
        if l is None:
            return Node(x, parent)

        if less(x, l.item, self.key):
            l.left = self._insert(l.left, x, l)
        elif less(l.item, x, self.key):
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

    def __iter__(self):
        """In order iterate through tree structure"""
        return inorder(self.root)


def inorder(tree: Node):
    """In order traversal"""
    if tree:
        # Recursively iterate over elements in the left sub-tree
        for l_child in inorder(tree.left):
            # Return left sub-tree data elements one-by-one
            yield l_child
        # Return data element from current node
        yield tree.item
        # Recursively iterate over elements in the right sub-tree
        for r_child in inorder(tree.right):
            # Return right sub-tree data elements one-by-one
            yield r_child


def preorder(tree: Node):
    """Pre order traversal"""
    if tree:
        # Return data element from current node
        yield tree.item

        # Recursively iterate over elements in the left sub-tree
        for l_child in preorder(tree.left):
            # Return left sub-tree data elements one-by-one
            yield l_child

        # Recursively iterate over elements in the right sub-tree
        for r_child in preorder(tree.right):
            # Return right sub-tree data elements one-by-one
            yield r_child


def postorder(tree: Node):
    """Post order traversal"""
    if tree:
        # Recursively iterate over elements in the left sub-tree
        for l_child in postorder(tree.left):
            # Return left sub-tree data elements one-by-one
            yield l_child

        # Recursively iterate over elements in the right sub-tree
        for r_child in postorder(tree.right):
            # Return right sub-tree data elements one-by-one
            yield r_child

        # Return data element from current node
        yield tree.item
