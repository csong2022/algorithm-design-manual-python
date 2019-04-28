from algorist.data_structure.priority_queue import PriorityQueue


def swap(s: list, i: int, j: int) -> None:
    if i != j:
        s[i], s[j] = s[j], s[i]


def insertion_sort(s: list, n: int) -> None:
    for i in range(1, n):
        j = i
        while j > 0 and s[j] < s[j - 1]:
            swap(s, j, j - 1)
            j -= 1


def selection_sort(s: list, n: int) -> None:
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if s[j] < s[min_index]:
                min_index = j
        swap(s, i, min_index)


def quicksort(s: list, l: int, h: int) -> None:
    if h > l:
        p = partition(s, l, h)
        quicksort(s, l, p - 1)
        quicksort(s, p + 1, h)


def partition(s: list, l: int, h: int) -> int:
    p = h
    first_high = l
    for i in range(l, h):
        if s[i] < s[p]:
            swap(s, i, first_high)
            first_high += 1
    swap(s, p, first_high)

    return first_high


def heapsort(s: list, n: int) -> None:
    q = PriorityQueue.make_heap(s, n)  # heap for heapsort

    for i in range(0, n):
        s[i] = q.extract_min()


def binary_search(s: list, key, low: int, high: int) -> int:
    if low > high:  # key not found
        return -1

    middle = (low + high) // 2  # index of middle element, this is integer divide
    if s[middle] == key:
        return middle
    elif s[middle] > key:
        return binary_search(s, key, low, middle - 1)
    else:
        return binary_search(s, key, middle + 1, high)


def mergesort(s: list, low: int, high: int) -> None:
    if low < high:
        aux = s[:]
        _mergesort(s, aux, low, high)


def _mergesort(s: list, aux: list, low: int, high: int) -> None:
    if low < high:
        middle = (low + high) // 2  # index of middle element, this is integer divide
        _mergesort(s, aux, low, middle)
        _mergesort(s, aux, middle + 1, high)

        _merge(s, aux, low, middle, high)


def _merge(s: list, aux: list, low: int, middle: int, high: int) -> None:
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
        elif aux[i] < aux[j]:
            s[k] = aux[i]
            i += 1
        else:
            s[k] = aux[j]
            j += 1


def is_sorted(s: list) -> bool:
    return all(s[i] <= s[i + 1] for i in range(len(s) - 1))
