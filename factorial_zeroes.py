#Given a positive integer n, write a function that finds the number of zeros at the end of n! in base 10.

#zeroesEndingFactorial(1)
# 0

#zeroesEndingFactorial(5)
# 1

#zeroesEndingFactorial(100)
# 24

import math

def zeroesEndingFactorial(int):
    fact = math.factorial(int)
    counter = 0
    arr = []
    for x in str(fact):
        arr.append(x)
    for i in reversed(arr):
        if i == '0':
            counter += 1
        else:
            break
    print(counter)

zeroesEndingFactorial(100)