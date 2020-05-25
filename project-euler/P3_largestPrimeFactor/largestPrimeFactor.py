# Largest prime factor
# Problem 3

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

from math import sqrt


def factorList(n):
    factors = []
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
    return factors


def isPrime(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    if len(factors) < 3:
        return True
    return False


n = 600851475143

primeFactors = []

for i in factorList(n):
    if isPrime(i):
        primeFactors.append(i)

print("Sol = ", primeFactors[-1])
