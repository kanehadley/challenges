#! /usr/bin/env python

import math
import itertools

def isprime(n):
    """Indicates if the integer is prime

    The integer is prime if none of the numbers from 2 to the square root of
    n divides n.

    :param n: An integer
    :return: True or False whether the integer is prime
    """

    return len(list(itertools.dropwhile(lambda x: n % x != 0, range(2, math.floor(math.sqrt(n) + 1))))) == 0

def prime_generator():
    """Iterator that produces prime numbers

    :return: The next highest prime number from the current one.
    """
    current = 2
    while True:
        if isprime(current):
            yield current
        current += 1

def p3 ():
    factors = filter(lambda x: 600851475143 % x == 0, range(math.ceil(math.sqrt(600851475143)) + 1, 1, -1))
    print(list(itertools.islice(itertools.dropwhile(lambda x: not p3.isprime(x), factors), 1))[0])
