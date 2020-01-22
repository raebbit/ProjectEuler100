"""
Project Euler: Problem 9: Special Pythagorean triplet
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc such that a + b + c = n.
"""
import math 

def pythagorean_triplet(n):
    for  a in range(1, int(n)//3):
        for b in range(a+1, int(n)//2):
            
            c_fromn = int(n) - a - b
            if c_fromn > b:

                c_pytha = math.sqrt(a**2 + b**2) # the result of sqrt is float
                if float(c_fromn) == c_pytha:
                    return a * b * c_fromn
                else:
                    continue

if __name__ == '__main__':
    n = input("a + b + c = ")
    print(pythagorean_triplet(n))
