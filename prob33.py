"""
Project Euler: Problem 33: Digit cancelling fractions

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe 
that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, 
and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""
# The only case that the 'cancelling' makes sense is, (10n + c)/(10c + d) = n/d. -> 1 <= n < d < c <= 9
import math 

def digit_cancelling_fractions():
    d_products = 1
    n_products = 1
    for n in range(1, 10):
        for d in range(n+1, 10):
            for c in range(d+1, 10):
                if (10 * n + c) * d == (10 * c + d) * n:
                    d_products *= d
                    n_products *= n

    return int(d_products / math.gcd(n_products, d_products))


if __name__ == '__main__':
    print(digit_cancelling_fractions())

