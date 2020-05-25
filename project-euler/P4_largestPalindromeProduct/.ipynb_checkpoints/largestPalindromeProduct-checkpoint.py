# Largest palindrome product
# Problem 4

# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

# largest number we can obtain by mltiplying 2 3-digit numbers:
# 999 * 999 = 998001

maxPal = 998001


def largestPalBelow(n):
    notLargestPal = True
    while notLargestPal:
        textPal = str(n)
        if textPal[0] == textPal[-1] and \
                textPal[1] == textPal[-2] and \
                textPal[2] == textPal[-3]:
            print(n)
            break
        n += -1
    return


largestPalBelow(maxPal)  # its 997799

# so we only need to focus on all ints between 100-998.
# if we reverse them we obtain all the palindromes.
# less than 100 they begin with a zero and only have 5 chars.
# larger and they are larger then what we want.

# might as well start from the largest down.
for i in reversed(range(100, 998)):
    pal = int(str(i) + str(i)[::-1])  # reverse the number and "glue" together
    factors = []  # calculate palindrome factors
    for j in range(100, 1000):  # we only care for those with 3 digits
        if pal % j == 0:
            factors.append(j)

    # print(pal, factors)

    if len(factors) > 1:  # we want the multiplication of 2 factors.
        a = 0
        while a < len(factors):  # to perform combinations
            b = a  # to stay in the upper triangle (do the drawing)
            while b < len(factors):
                if factors[a] * factors[b] == pal:
                    print("pal ", pal, "|",
                          factors[a], "*", factors[b], "=",
                          factors[a] * factors[b])
                b += 1
            a += 1
