"""
Project Euler: Problem 26: Reciprocal cycles
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2 = 0.5
1/3 = 0.(3)
1/4 = 0.25
1/5 = 0.2
1/6 = 0.1(6)
1/7 = 0.(142857)
1/8 = 0.125
1/9 = 0.(1)
1/10 = 0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < n for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""
# 1. Make decimal into str and check if there is a cycle   2. Using Fermat's Theorem (10^n mod p = 1, n = p-1 or n | p-1)
# Let's do #2. From the formula, n is the length of the recurring cycle of 1/p.(I understand it... intuitively but, don't know how to prove)
# I know that according to the Fermat's theorem, 10^n/p and 1/p has the same decimal representation below the decimal point.

def is_prime(number):
    i = 2
    while i*i <= number:
        if number % i == 0:
            return False
        i += 1
    return True

def reciprocal_cycles(n):
    primes_below_n = []
    for i in range(int(n), 1, -1): # checking bigger primes first is faster
        if is_prime(i):
            primes_below_n.append(i)

    for p in primes_below_n:
        c = 1
        while pow(10, c, p) != 1:
            c += 1
        
        if p - c == 1:
            break

    return p

if __name__ == '__main__':
    n = input("n ? : ")
    print(reciprocal_cycles(n))
