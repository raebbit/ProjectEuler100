"""
Project Euler: Problem 10: Summation of primes
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below n. (website: below two million)
"""
# Except 2 and 3, primes are written in the form of 6k±1.
# Beware of the pseudo-prime!
import math

def is_prime(number):
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False
        else:
            continue
    return True

def prime_summation(n):
    prime_sum = 0
    prime_i = [5, 7]
    
    if int(n) == 3:
        prime_sum = 2
    elif int(n) == 4:
        prime_sum = 5
    elif int(n) >= 5:
        prime_sum = 5  #2 + 3 = 5
        for prime in prime_i:
            while prime < int(n):
                if is_prime(prime):
                    prime_sum += prime
                prime += 6
                
    return prime_sum

if __name__ == '__main__':
    n = input("Sum of primes below n, n ?: ")
    print(prime_summation(n))
        
