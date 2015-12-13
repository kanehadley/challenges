#! /usr/bin/env python

from itertools import dropwhile, filterfalse
from math import sqrt, floor, ceil


def fibonnaci_generator():
    """Generates an iterator for the Fibonnaci sequence.

    :return: Iterator
    """
    def fibonnaci():
        """Iterator that returns the Fibonnaci sequence.

        :return: Each yield gives the next Fibonnaci number in the sequence.
        """
        previous = 1
        current = 1

        while True:
            yield current
            temp = current
            current += previous
            previous = temp

    return fibonnaci()


def isprime(n):
    """Indicates if the integer is prime

    The integer is prime if none of the numbers from 2 to the square root of
    n divides n.

    :param n: An integer
    :return: True or False whether the integer is prime
    """

    return len(list(
            dropwhile(lambda x: n % x != 0,
                      range(2, floor(sqrt(n) + 1))))) == 0


def prime_generator():
    """Iterator that produces prime numbers

    :return: The next highest prime number from the current one.
    """
    current = 2
    while True:
        if isprime(current):
            yield current
        current += 1

def is_palindrome_int(n):
    """Checks if n is a palindrome

    :param n: integer
    :return: True or False if n is a palindrome
    """
    return len(list(filterfalse(None,
                                map(lambda x, y: x == y,
                                    str(n),
                                    reversed(str(n)))))) == 0


def factorize(n, factors_superset):
    """

    :param n: Integer to be factored.
    :param factors: List of possible integers that can divide n.
    :return: Factorization of n based on the values in factors. May have
        duplicates of some factors.
    """
    factors = filter(lambda x: 1 != x, factors_superset)
    start = list(dropwhile(lambda x: n % x != 0, sorted(factors)))
    if 0 == len(start):
        return [int(n)]
    else:
        return [start[0]] + factorize(int(n / start[0]), factors_superset)


def prime_factorization(n):
    """Finds the prime factors for an integer, n

    :param n: Integer to factor.
    :return: list - The prime factors for the integer
    """

    # Grab all possible prime factors
    primes = list(filter(lambda x: isprime(x), range(2, ceil(sqrt(n)) + 1)))

    if 1 == n:
        return [1]

    if isprime(n):
        return [1, n]

    return factorize(n, primes)
