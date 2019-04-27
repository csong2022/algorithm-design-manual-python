MAXINT = 100000  # infinity


def read_partition(input):
    n, k = list(map(int, input.readline().split()))
    s = [0] * (n + 1)
    for i in range(1, n + 1):
        s[i] = int(input.readline()[:-1])

    return s, n, k


def print_books(s, start, end):
    print("{", end='')
    for i in range(start, end + 1):
        print(" %d " % s[i], end='')
    print('}')


def print_matrix(m, n, k):
    print()
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            print(" %d " % m[i][j], end='')
        print()


def reconstruct_partition(s, d, n, k):
    if k == 1:
        print_books(s, 1, n)
    else:
        reconstruct_partition(s, d, d[n][k], k - 1)
        print_books(s, d[n][k] + 1, n)


def partition(s, n, k):
    p = [0] * (n + 1)  # prefix sums array
    m = [[0] * (k + 1) for i in range(n + 1)]  # DP table for values
    d = [[0] * (k + 1) for i in range(n + 1)]  # DP table for dividers

    p[0] = 0  # construct prefix sums
    for i in range(1, n + 1):
        p[i] = p[i - 1] + s[i]
    for i in range(1, n + 1):
        m[i][1] = p[i]  # initialize boundaries
    for j in range(1, k + 1):
        m[1][j] = s[1]

    for i in range(2, n + 1):  # evaluate main recurrence
        for j in range(2, k + 1):
            m[i][j] = MAXINT
            for x in range(1, i):
                cost = max(m[x][j - 1], p[i] - p[x])
                if m[i][j] > cost:
                    m[i][j] = cost
                    d[i][j] = x

    reconstruct_partition(s, d, n, k)  # print book partition
