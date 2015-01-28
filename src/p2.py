def p2 ():
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


