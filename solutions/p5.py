#! /usr/bin/env python

from math import sqrt, ceil
from itertools import dropwhile
from functools import reduce
import collections

from toolset import prime_factorization




def p5():
    values = range(1, 21)
    counters = list(map(lambda x: collections.Counter(prime_factorization(x)),
                        values))
    return reduce(lambda x, y: x*y,
                  list(reduce(lambda x, y: x + (y - (y & x)),
                              counters,
                              collections.Counter()).elements()),
                  1)

