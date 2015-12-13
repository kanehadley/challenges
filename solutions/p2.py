#! /usr/bin/env python

from itertools import takewhile

import toolset


def p2():
    fibonnaci = toolset.fibonnaci_generator()
    print(sum(filter(lambda x: x % 2 == 0,
                     takewhile(lambda x: x < 4000000, fibonnaci))))

