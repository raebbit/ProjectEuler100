"""
Project Euler: Problem 49: Prime permutations
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: 
(i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, 
but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""
from itertools import permutations

def is_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def is_permutation(x, y):
    permu_x = list(permutations(str(x)))
    permutation_x = []
    for tup in permu_x:
        permutation_x.append(''.join(tup))
    
    if str(y) in permutation_x:
        return True
    else:
        return False


def prime_permutation_arithmetic():
    prime_4digit = []
    for x in range(1001, 10000):
        if is_prime(x):
            if x not in [1487, 4817, 8147]:
                prime_4digit.append(x)
    
    for first in prime_4digit:
        for second in prime_4digit:
            if first != second and is_permutation(first, second):
                third = second + (second - first)
                if third in prime_4digit:
                    if is_permutation(first, third):
                        return str(first) + str(second) + str(third)
                

if __name__ == '__main__':
    print(prime_permutation_arithmetic())
    #print(is_permutation(1234, 1423))