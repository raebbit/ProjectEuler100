"""
Project Euler: Problem 40: Champernowne's constant
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""
# d1 = 1, d10 = 1
# (a, b, c) = (a-digit group, bth number in the group, cth digit of b)
import math 

def Champernowne_const(n): # dn
    total_up = 0
    a = 0
    while n > total_up:
        a += 1
        total_up += pow(10, a-1) * 9  * a

    total_bf_a = total_up - pow(10, a-1) * 9 * a
    b = math.ceil((n - total_bf_a) / a)   # math.ceil -> round up

    c = n - total_bf_a - (a * (b-1))

    return str(pow(10, a-1) + (b-1))[c-1]
    
    
if __name__ == '__main__':
    answer = 1
    for i in [100, 1000, 10000, 100000, 1000000]:
        answer *= int(Champernowne_const(i))
    print(answer)
    