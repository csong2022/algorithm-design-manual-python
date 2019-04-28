from unittest import TestCase

from algorist.data_structure.linked_queue import Queue
from algorist.data_structure.war import rank_card, war
from tests.algorist.test.test_engine import execute


class TestWar(TestCase):

    def process(self, input):
        decks = [Queue(), Queue()]
        while True:
            for i in range(2):
                line = input.readline()
                if not line:
                    return
                deck = Queue()

                j = 0
                while j < len(line) - 1:
                    c = line[j]
                    j += 1
                    if c != ' ':
                        value = c
                        suite = line[j]
                        j += 1
                        deck.enqueue(rank_card(value, suite))

                decks[i] = deck

            war(decks[0], decks[1])

    def test(self):
        execute(self, "war-in", "war-out")
