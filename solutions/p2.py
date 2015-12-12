def p2 ():
    '''
        Iterates over all the fibonnaci numbers less than 4 million and sums them
        up. Next time try a python Generator instead of this iterative loop.
    '''
    total = 0
    previous = 1
    current = 1

    while current < 4000000:
        if current % 2 == 0:
            total += current
        temp = current
        current += previous
        previous = temp

    print total


