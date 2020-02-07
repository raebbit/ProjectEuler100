"""
Project Euler: Problem 7: 10001st prime
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the nth prime number? (website: 10001st prime number?)
"""
import math
def is_prime(number):
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False
        else: 
            continue
    
    return True


def nth_prime(n):
    nth = int(n)
    prime = 3
    count = 2

    while count < nth:
        prime += 2
        if is_prime(prime):
            count += 1
      
    else:
        if nth == 1:
            return 2
        elif nth == 2:
            return 3
        else:
            return prime

if __name__ == '__main__':
    n = input("n ?: ")
    print(nth_prime(n))