def gcdIter(a, b):
    
    c = a + b

    while c > 0:
        if a % c == 0 and b % c == 0:
            return c
        c -= 1
    return 1
