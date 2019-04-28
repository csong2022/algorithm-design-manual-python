# -*- coding: utf-8 -*-
"""
Compute the number of circles in two different disk packings.
Assuming we have an $w \times l$ box, how many unit disks
can we pack in there assumming we have w disks on the bottom?

Translate from plates.c.
"""

from math import sqrt, floor, ceil


def dense_layers(w: float, h: float, r: float) -> int:
    """how many triangular-lattice layers of radius r balls fit in height h? """
    if 2 * r > h:
        return 0

    gap = 2.0 * r * (sqrt(3.0) / 2.0)
    return 1 + floor((h - 2.0 * r) / gap)


def plates_per_row(row: int, w: float, r: float) -> int:
    plates_per_full_row = floor(w / (2 * r))  # number of plates in full/even row

    if (row % 2) == 0:
        return plates_per_full_row

    if ((w / (2 * r)) - plates_per_full_row) >= 0.5:  # odd row full, too
        return plates_per_full_row
    else:
        return plates_per_full_row - 1


def dense_plates(w: float, l: float, r: float) -> int:
    layers = dense_layers(w, l, r)

    return ceil(layers / 2.0) * plates_per_row(0, w, r) + \
           floor(layers / 2.0) * plates_per_row(1, w, r)


def grid_plates(w: float, h: float, r: float) -> int:
    layers = floor(h / (2 * r))
    return layers * plates_per_row(0, w, r)


def hex_to_geo(xh: int, yh: int, r: float) -> tuple:
    yg = (2.0 * r) * xh * (sqrt(3) / 2.0)
    xg = (2.0 * r) * xh * (1.0 / 2.0) + (2.0 * r) * yh

    return xg, yg


def geo_to_hex(xg: float, yg: float, r: float) -> tuple:
    xh = (2.0 / sqrt(3)) * yg / (2.0 * r)
    yh = (xg - (2.0 * r) * (xh) * (1.0 / 2.0)) / (2.0 * r)

    return xh, yh


def array_to_hex(xa: int, ya: int) -> tuple:
    xh = xa
    yh = ya - xa + ceil(xa / 2.0)
    return xh, yh


def hex_to_array(xh: int, yh: int) -> tuple:
    xa = xh
    ya = yh + xh - ceil(xh / 2.0)

    return xa, ya


def plates_on_top(xh: int, yh: int, w: float, l: float, r: float) -> int:
    number_on_top = 0  # total plates on top
    layers = dense_layers(w, l, r)  # number of rows in grid

    for row in range(xh + 1, layers):
        rowlength = plates_per_row(row, w, r) - 1  # number of plates in row

        _, yla = hex_to_array(row, yh - (row - xh))
        if yla < 0:  # left boundary
            yla = 0

        _, yra = hex_to_array(row, yh)
        if yra > rowlength:  # right boundary
            yra = rowlength

        number_on_top += yra - yla + 1

    return number_on_top
