# Rank the desirability of suitors -- sorting example.

class Suitor:
    def __init__(self, first: str, last: str, height: int, weight: int):
        self.first = first  # suitor's first name
        self.last = last  # suitor's last name
        self.height = height  # suitor's height
        self.weight = weight  # suitor's weight

    def __str__(self):
        return "%s,%s,%d,%d" % (self.last, self.first, self.height, self.weight)


BESTHEIGHT = 180  # best height in centimeters
BESTWEIGHT = 75  # best weight in kilograms


def read_suitors(input) -> list:
    suitors = []

    while True:
        line = input.readline()
        if not line:
            break
        values = line.split()
        first = values[0]
        last = values[1]

        height = int(values[2])
        height = abs(height - BESTHEIGHT)

        weight = int(values[3])
        if weight > BESTWEIGHT:
            weight -= BESTWEIGHT
        else:
            weight = -weight
        suitors.append(Suitor(first, last, height, weight))

    return suitors


def suitor_compare(a: Suitor, b: Suitor) -> int:
    if a.height < b.height:
        return -1
    if a.height > b.height:
        return 1

    if a.weight < b.weight:
        return -1
    if a.weight > b.weight:
        return 1

    if a.last < b.last:
        return -1
    if a.last > b.last:
        return 1

    if a.first < b.first:
        return -1
    if a.first > b.first:
        return 1

    return 0
