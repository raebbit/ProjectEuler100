"""
Project Euler: Problem 43: Sub-string divisibility
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, 
but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2

d3d4d5=063 is divisible by 3

d4d5d6=635 is divisible by 5

d5d6d7=357 is divisible by 7

d6d7d8=572 is divisible by 11

d7d8d9=728 is divisible by 13

d8d9d10=289 is divisible by 17

Find the numbers of all 0 to 9 pandigital numbers with this property.
"""
from itertools import permutations

def is_property_right(number):
    primes = [2, 3, 5, 7, 11, 13, 17]
    for i in range(7):
        if int(str(number)[i+1:i+4]) % primes[i] != 0:
            return False
    
    return True


def substring_divisibility():
    permu = list(permutations('0123456789'))
    numbers = []
    for tup in permu[362880:]: # except when the first digit is 0 (9! = 362880)
        numbers.append(''.join(tup))
    
    sum_num = 0
    for number in numbers:
        if is_property_right(number):
            sum_num += int(number)

    return sum_num


if __name__ == '__main__':
    # print(is_property_right(1406357289))
    print(substring_divisibility())