"""
Project Euler: Problem 47: Distinct primes factors
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5
The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19
Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
"""
import math

def distinct_num_pf(n): # from prob3
    prime_factors = set()
    # prime factor 2
    while n % 2 == 0:
        prime_factors.add(2)
        n = n / 2
    
    # prime factor bigger than 2
    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            prime_factors.add(i)
            n = n / i

    # if the last factor is prime
    if n > 2:
        prime_factors.add(n)
    
    return len(prime_factors)


def distinct_primes_factors(num_primes, num_consecutive): # the way of using bool is similar to prob46.py
    notfound = True
    first_num = 1
    while notfound:
        first_num += 1
        num_conse_found = True
        if distinct_num_pf(first_num) == num_primes:
            for i in range(1, num_consecutive):
                if distinct_num_pf(first_num + i) != num_primes:
                    num_conse_found = False
                    break
            
            if num_conse_found == True:
                notfound = False
    
    return first_num


if __name__ == '__main__':
    print(distinct_primes_factors(4, 4))
            

            

            