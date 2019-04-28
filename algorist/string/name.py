# -*- coding: utf-8 -*-
"""
Corporate name changing program -- string example

Translate from name.c.
"""
# Corporate name changing program -- string example


def read_changes(_input) -> list:
    mergers = []
    nmergers = int(_input.readline()[:-1])

    for i in range(nmergers):
        line = _input.readline()
        mergers.append(read_quoted_strings(line[:-1]))
    return mergers


def read_quoted_strings(s) -> list:
    names = []

    j = 0
    for i in range(2):
        while j < len(s) and s[j] != '"':
            j += 1
        start = j + 1
        j += 2
        while j < len(s) and s[j] != '"':
            j += 1
        end = j
        j += 2
        names.append(s[start: end])

    return names


def findmatch(p: str, t: list) -> int:
    """
    :param p: pattern.
    :param t: list of characters.
    :return: the position of the first occurrence of the pattern p in the text t,
        and -1 if it does not occur.
    """
    plen = len(p)
    tlen = len(t)

    for i in range(tlen - plen + 1):
        j = 0
        while j < plen and t[i + j] == p[j]:
            j += 1
        if j == plen:
            return i

    return -1


def replace_x_with_y(s: list, slen: int, pos: int, xlen: int, y: str) -> int:
    """
    Replace the substring of length xlen starting at position pos in
    string s with the contents of string y.

    :param s: list of characters.
    :param slen: text length.
    :param pos: starting position.
    :param xlen: length to be replaced.
    :param y: new name.
    :return: length of new text
    """
    ylen = len(y)

    if xlen >= ylen:
        for i in range(pos + xlen, slen + 1):
            s[i + (ylen - xlen)] = s[i]
    else:
        for i in range(slen, pos + xlen - 1, -1):
            s[i + (ylen - xlen)] = s[i]

    for i in range(ylen):
        s[pos + i] = y[i]

    return slen + (ylen - xlen)


def process_mergers(s: list, slen: int, mergers: list) -> int:
    for j in range(len(mergers)):
        while True:
            pos = findmatch(mergers[j][0], s)
            if pos == -1:
                break
            slen = replace_x_with_y(s, slen, pos, len(mergers[j][0]), mergers[j][1])

    return slen
