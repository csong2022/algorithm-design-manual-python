# -*- coding: utf-8 -*-
"""
Simulation of the children's card game War

Read in cards with format value, suit, e.g. 4h ranked by orders 23456789TJQKA and cdhs
"""
import random

from algorist.data_structure.linked_queue import Queue

NGAMES = 50
MAXSTEPS = 100000

NCARDS = 52  # number of cards
NSUITS = 4  # number of suits

values = "23456789TJQKA"
suits = "cdhs"


def rank_card(value: str, suit: str) -> int:
    for i in range(NCARDS // NSUITS):
        if values[i] == value:
            for j in range(NSUITS):
                if suits[j] == suit:
                    return i * NSUITS + j

    print("Warning: bad input value=%c, suit=%c" % (value, suit))
    return -1


# Return the suit and value of the given card.
def suit(card: int) -> str:
    return suits[card % NSUITS]


def value(card: int) -> str:
    return values[card // NSUITS]


def testcards() -> None:
    for i in range(NCARDS):
        print(" i=%d card[i]=%c%c rank=%d" %
              (i, value(i), suit(i), rank_card(value(i), suit(i))))


def random_init_deck(a: Queue, b: Queue) -> None:
    perm = [0] * NCARDS

    for i in range(NCARDS):
        perm[i] = i

    random.shuffle(perm)

    a = Queue()
    b = Queue()

    for i in range(NCARDS // 2):
        a.enqueue(perm[2 * i])
        b.enqueue(perm[2 * i + 1])

    print_card_queue(a)
    print_card_queue(b)


def war(a: Queue, b: Queue) -> None:
    steps = 0  # step counter
    inwar = False  # are we involved in a war?
    c = Queue()  # cards involved in the war

    while not a.is_empty() and (not b.is_empty() and steps < MAXSTEPS):
        steps += 1
        x = a.dequeue()
        y = b.dequeue()
        c.enqueue(x)
        c.enqueue(y)

        if inwar:
            inwar = False
        else:
            if value(x) > value(y):
                clear_queue(c, a)
            elif value(x) < value(y):
                clear_queue(c, b)
            elif value(y) == value(x):
                inwar = True

    if not a.is_empty() and b.is_empty():
        print("a wins in %d steps " % steps)
    elif a.is_empty() and not b.is_empty():
        print("b wins in %d steps " % steps)
    elif not a.is_empty() and not b.is_empty():
        print("game tied after %d steps, |a|=%d |b|=%d " %
              (steps, a.size(), b.size()))
    else:
        print("a and b tie in %d steps " % steps)


def print_card_queue(q: Queue) -> None:
    for value in q:
        print("%c%c " % (value(value), suit(value)))
    print()


def clear_queue(a: Queue, b: Queue) -> None:
    while not a.is_empty():
        b.enqueue(a.dequeue())
