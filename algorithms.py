import math
from fractions import Fraction
# rounding to the nearest given number
# finding the maximum or minimum number in a list
# finding the average of a set of numbers in a list
# hailstone numbers
# find all prime numbers less than a given value
# difficult, given prime factorisation of a number find all factors of a number

# rounding
# for number m rounded to the nearest number n
# divide m by n
# round the result
# multiply n

def roundTo(m, n):
    return Fraction(round(m/n)*n).limit_denominator()

print(roundTo(31/15,1/7))
print(roundTo(-8,10))
