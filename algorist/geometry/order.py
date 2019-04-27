# Demonstrate traversal orders on a grid.

def row_major(n, m):
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            process(i, j)


def column_major(n, m):
    for j in range(1, m + 1):
        for i in range(1, n + 1):
            process(i, j)


def snake_order(n, m):
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            process(i, j + (m + 1 - 2 * j) * ((i + 1) % 2))


def diagonal_order(n, m):
    for d in range(1, m + n):
        height = 1 + max(0, d - m)
        pcount = min(d, (n - height + 1))
        for j in range(pcount):
            process(min(m, d) - j, height + j)


def process(i, j):
    print("(%d,%d)" % (i, j))
