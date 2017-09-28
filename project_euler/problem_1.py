# Problem Euler #1: Multiples of 3 and 5
#
# Author: Dickson Wong
# Date: September 28, 2017
# python 3.4
#
# tags: multiples, floating point
##
import math

# An old solution from 2011
def problem_1(n):
    '''Add all the natural numbers below n that are multiples
    of 3 or 5.'''

    total = 0

    for i in range(0,n):
        if i % 5 == 0 or i % 3 == 0:
            total = total + i

    print(total)

# A better way of solving the problem would be to simply take the sum
# between all multiples of 3 or 5 through simple arithmetic series

# Unfortunately, taking the sum of all multiples of 3 and all multiples of
# 5 results in adding duplicates; as a result, one simply needs to subtract
# all multiples of 15.

# This results in:
# SUM = (1/2) (N1 * (3 + 999) + N2 * (5 + 1000) - N3 * (15 + 990))
# with
# N1: number of multiples of 3
# N2: number of multiples of 5
# N3: number of multiples of 15

# This would be an O(1) solution as opposed to O(n), with n being the upper
# bound on the values (in this case n = 1000)

# This solution has issues with large values of n; rounding issues occur
def sum_of_multiples(n):
    ''' (int) -> int
    Returns the sum of all integers below n that is a multiple of 3 or 5.
    '''
    n = n - 1
    sum = 0

    if n > 2:
        n1 = math.floor(n / 3)
        sum += n1 * (3 + n1 * 3)

    if n > 14:
        n3 = math.floor(n / 15)
        sum -= n3 * (15 + n3 * 15)

    if n > 4:
        n2 = math.floor(n / 5)
        sum += n2 * (5 + n2 * 5)

    return math.floor(sum / 2)

# This solution attempts to solve floating point issues through rewriting
# the calculation to remove all occurrances of rounding
def sum_of_multiples_better_rounding(n):
    ''' (int) -> int
    Returns the sum of all integers below n that is a multiple of 3 or 5.
    '''
    n = n - 1
    sum = 0

    n1 = math.floor(n / 3)
    n2 = math.floor(n / 5)
    n3 = math.floor(n / 15)

    if n1 > 0:
        sum += n1 * 3
        if n1 % 2 == 0:
            sum += math.floor(n1 / 2) * 3 * (n1 - 1)
        else:
            sum += n1 * 3 * math.floor((n1 - 1) / 2)

    if n2 > 0:
        sum += n2 * 5
        if n2 % 2 == 0:
            sum += math.floor(n2 / 2) * 5 * (n2 - 1)
        else:
            sum += n2 * 5 * math.floor((n2 - 1) / 2)

    if n3 > 0:
        sum -= n3 * 15
        if n3 % 2 == 0:
            sum -= math.floor(n3 / 2) * 15 * (n3 - 1)
        else:
            sum -= n3 * 15 * math.floor((n3 - 1) / 2)

    return sum

if __name__ == "__main__":
    n = 1000000
    problem_1(n)
    print(sum_of_multiples_better_rounding(n))