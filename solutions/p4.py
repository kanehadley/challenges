#! /usr/bin/env python

from itertools import starmap, product

import toolset


def p4 ():
    return list(filter(lambda x: toolset.is_palindrome_int(x),
                       reversed(sorted(starmap(lambda x, y: x*y,
                                               product(range(100, 1000),
                                                       repeat=2))))))[0]
