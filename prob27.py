"""
Project Euler: Problem 27: Quadratic primes
Euler discovered the remarkable quadratic formula:

n^2+n+41 
It turns out that the formula will produce 40 primes for the consecutive integer values  0≤n≤39 . 
However, when  n=40,402+40+41=40(40+1)+41  is divisible by 41, and certainly when  n=41,412+41+41  is clearly divisible by 41.

The incredible formula  n2−79n+1601  was discovered, which produces 80 primes for the consecutive values  0≤n≤79. 
The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n^2+an+b , where  |a|<range  and  |b|≤range where  |n|  is the modulus/absolute value of  n (e.g.  |11|=11  and  |−4|=4 )

Find the product of the coefficients,  a  and  b , 
for the quadratic expression that produces the maximum number of primes for consecutive values of  n , starting with  n=0 .
"""
import math
def is_prime(number):
    if number < 1: # if quadratic is negative
        return False
    for i in range(2, int(math.sqrt(number))+1):
        if number % i == 0:
            return False

    return True


def quadratic_primes(ab_range):
    # when n=0, 0+0+b must be a prime number. So b sould be primes within the range.
    b_range = []
    for j in range(2, int(ab_range)+1):
        if is_prime(j):
            b_range.append(j)

    # when n=1, 1+a+b>1(prime>1). So I got a > -b. 
    # And when n=b, b^2+ab+b is clearly not a prime, so n < b.
    max_a, max_b = 0, 0
    max_n = 0
    for b in b_range:
        for a in range(-b+1, int(ab_range)):
            n = 0
            while n < b:
                quadratic = n*n + a*n + b
                if is_prime(quadratic) == False:
                    break
                else:
                    n += 1
            
            if n > max_n:
                max_n = n
                max_a = a
                max_b = b

    return max_a * max_b

if __name__ == '__main__':
    ab_range = input("Set the range for a and b: ")
    print(quadratic_primes(ab_range))
        