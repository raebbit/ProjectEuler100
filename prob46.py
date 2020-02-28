"""
Project Euler: Problem 46: Goldbach's other conjecture
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2

15 = 7 + 2×2^2

21 = 3 + 2×3^2

25 = 7 + 2×3^2

27 = 19 + 2×2^2

33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""
import math

def is_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False # composite

        i += 1
    return True # prime

def goldbachs_other_conjecture():
    notfound = True
    k = 4 
    while notfound:
        k += 1
        odd = 2 * k - 1
        goldbachs = False
        if is_prime(odd) == False: 
            for i in range(1, int(math.sqrt(odd/2))+1):
                con_prime = odd - (2 * i * i)
                if is_prime(con_prime):
                    goldbachs = True
                    break
            
            if goldbachs == False:
                notfound = False

    return odd

if __name__ == '__main__':
    print(goldbachs_other_conjecture())