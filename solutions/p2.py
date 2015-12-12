#! /usr/bin/env python

import itertools


def fibonnaci():
    previous = 1
    current = 1

    while True:
        yield current
        temp = current
        current += previous
        previous = temp


def p2():
    print(sum(filter(lambda x: x % 2 == 0,
                     itertools.takewhile(lambda x: x < 4000000, fibonnaci()))))

