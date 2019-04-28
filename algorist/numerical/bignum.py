import copy

MAXDIGITS = 100  # maximum length bignum
PLUS = 1  # positive sign bit
MINUS = -1  # negative sign bit

DIGITS = "0123456789"


class Bignum:
    """
    	Implementation of large integer arithmetic: addition, subtraction,
		multiplication, and division.
    """

    def __init__(self):
        self.digits = [0] * MAXDIGITS  # represent the number
        self.signbit = 0  # 1 if positive, -1 if negative
        self.lastdigit = -1  # index of high-order digit
        #int_to_bignum(0, self)

    def print(self):
        if self.signbit == MINUS:
            print("- ", end='')

        for i in range(self.lastdigit, -1, -1):
            print("%c" % DIGITS[self.digits[i]], end='')
        print()


def int_to_bignum(s: int, n: Bignum):
    n.signbit = PLUS if s >= 0 else MINUS

    for i in range(MAXDIGITS):
        n.digits[i] = 0
    n.lastdigit = -1

    t = abs(s)

    while t > 0:
        n.lastdigit += 1
        n.digits[n.lastdigit] = t % 10
        t = t // 10

    if s == 0:
        n.lastdigit = 0

    return n


def add_bignum(a: Bignum, b: Bignum) -> Bignum:
    if a.signbit != b.signbit:
        if a.signbit == MINUS:
            a.signbit = PLUS
            c = subtract_bignum(b, a)
            a.signbit = MINUS
        else:
            b.signbit = PLUS
            c = subtract_bignum(a, b)
            b.signbit = MINUS
        return c
    else:
        c = Bignum()
        c.signbit = a.signbit

        c.lastdigit = max(a.lastdigit, b.lastdigit) + 1
        carry = 0

        for i in range(c.lastdigit + 1):
            c.digits[i] = (carry + a.digits[i] + b.digits[i]) % 10
            carry = (carry + a.digits[i] + b.digits[i]) // 10

        zero_justify(c)
        return c


def subtract_bignum(a: Bignum, b: Bignum) -> Bignum:
    c = Bignum()
    int_to_bignum(0, c)

    if (a.signbit == MINUS) or (b.signbit == MINUS):
        b.signbit = -1 * b.signbit
        c = add_bignum(a, b)
        b.signbit = -1 * b.signbit
        return c

    if compare_bignum(a, b) == PLUS:
        c = subtract_bignum(b, a)
        c.signbit = MINUS
        return c

    c.lastdigit = max(a.lastdigit, b.lastdigit)
    borrow = 0

    for i in range(c.lastdigit + 1):
        v = a.digits[i] - borrow - b.digits[i] # placeholder digit
        if a.digits[i] > 0:
            borrow = 0
        if v < 0:
            v += 10
            borrow = 1

        c.digits[i] = v % 10

    zero_justify(c)
    return c


def compare_bignum(a: Bignum, b: Bignum) -> int:
    if a.signbit == MINUS and b.signbit == PLUS:
        return PLUS

    if a.signbit == PLUS and b.signbit == MINUS:
        return MINUS

    if b.lastdigit > a.lastdigit:
        return PLUS * a.signbit

    if a.lastdigit > b.lastdigit:
        return MINUS * a.signbit

    for i in range(a.lastdigit, -1, -1):
        if a.digits[i] > b.digits[i]:
            return MINUS * a.signbit
        if b.digits[i] > a.digits[i]:
            return PLUS * a.signbit

    return 0


def zero_justify(n: Bignum) -> None:
    while n.lastdigit > 0 and n.digits[n.lastdigit] == 0:
        n.lastdigit -= 1

    if n.lastdigit == 0 and n.digits[0] == 0:
        n.signbit = PLUS  # hack to avoid -0


def digit_shift(n: Bignum, d: int) -> None:
    if n.lastdigit == 0 and n.digits[0] == 0:
        return

    for i in range(n.lastdigit, -1, -1):
        n.digits[i + d] = n.digits[i]

    for i in range(d):
        n.digits[i] = 0

    n.lastdigit += d


def multiply_bignum(a: Bignum, b: Bignum) -> Bignum:
    c = Bignum()
    int_to_bignum(0, c)

    row = copy.deepcopy(a)
    for i in range(b.lastdigit + 1):
        for j in range(1, b.digits[i] + 1):
            tmp = add_bignum(c, row)
            c = tmp
        digit_shift(row, 1)

    c.signbit = a.signbit * b.signbit
    zero_justify(c)

    return c


def divide_bignum(a: Bignum, b: Bignum) -> Bignum:
    c = Bignum()
    int_to_bignum(0, c)

    c.signbit = a.signbit * b.signbit

    asign = a.signbit
    bsign = b.signbit

    a.signbit = PLUS
    b.signbit = PLUS

    row = Bignum()
    int_to_bignum(0, row)

    c.lastdigit = a.lastdigit

    for i in range(a.lastdigit, -1, -1):
        digit_shift(row, 1)
        row.digits[0] = a.digits[i]
        c.digits[i] = 0

        while compare_bignum(row, b) != PLUS:
            c.digits[i] += 1
            tmp = subtract_bignum(row, b)
            row = tmp

    zero_justify(c)
    a.signbit = asign
    b.signbit = bsign
    return c
