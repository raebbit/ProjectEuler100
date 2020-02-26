"""
Project Euler: Problem 41: Pandigital prime
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. 
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-length digit pandigital prime that exists?
"""
# For 1 <= n <= 9, all the n-digit pandigital number is multiple of 3 except when n = 4 or 7.
# Since we have to find the largest, we start from 7-digit primes. (If there is no pandigital prime, we search 4-digit.)
from itertools import permutations

def is_prime(n):
    i = 2 
    while i * i <= int(n):
        if int(n) % i == 0:
            return False

        i += 1
    
    return True

def pandigital_prime():
    # 1234567 ~ 7654321
    permu = list(permutations('1234567'))
    numbers = []
    for tup in permu:
        numbers.append(''.join(tup))

    primes = []
    for number in numbers:
        if is_prime(number):
            primes.append(number)

    # max는 str 일때도 되는둡
    return max(primes)

if __name__ == '__main__':
    print(pandigital_prime())

