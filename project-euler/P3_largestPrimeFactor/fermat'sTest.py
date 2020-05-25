import numpy as np


def fermatsTest(p):
    print("\n p = ", p)
    A = []
    for a in np.arange(2, p, 1):
        print(a, "(=a)^", p-1, "(=p-1) %", p, "(=p) = ", np.power(a, p-1) % p)
        if np.power(a, p-1) % p != 1:
            A.append(a)
    print(A)
    return


for i in np.arange(3, 25, 2):
    fermatsTest(i)
