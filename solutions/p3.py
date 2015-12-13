#! /usr/bin/env python

from math import ceil, sqrt
from itertools import islice, dropwhile

import toolset


def p3():
    factors = filter(lambda x: 600851475143 % x == 0,
                     range(ceil(sqrt(600851475143)) + 1, 1, -1))
    print(list(islice(dropwhile(lambda x: not toolset.isprime(x),
                                factors), 1))[0])
