"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the given number? (fCC)
(Website: What is the largest prime factor of the number 600851475143 ?)
"""

# 소인수분해하기 

import math 

def largest_primefactor(n):
    number = int(n)
    prime_factors = []

    while number % 2 == 0:  # put all 2-factors in the list
        prime_factors.append(2)
        number = number / 2

    # check the factors(which is also prime-cuz it's gonna be divided) which is bigger than 3 and odd
    for i in range(3, int(math.sqrt(number))+1, 2): 
        while number % i == 0:
            prime_factors.append(i)
            number = number / i
    
    # if number(the last factor) is prime
    if number > 2:
        prime_factors.append(int(number))

    return max(prime_factors)

if __name__ == '__main__':
    n = input("Insert the number bigger than 1: ")
    print("The Largest Prime Factor: " + str(largest_primefactor(n)))
