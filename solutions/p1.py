#!/usr/bin/env python


def p1(n):
    """ Sums the numbers between 0 and n that are multiples of 3 and 5.

    :param n: The integer we're finding the sums of.
    """
    return sum([x for x in range(0, n) if x % 3 == 0 or x % 5 == 0])
