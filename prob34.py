"""
Project Euler: Problem 34: Digit factorials
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the numbers and the sum of the numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
# Since 9! = 326880, I assume that the numbers are less than 1,000,000(7 digits).
# There are no 1-digit number nor 2-digit (!)

from math import factorial

def digit_factorial():
    the_numbers = []
    for number in range(100, 1000000):
        sum_i = 0
        for i in str(number):
            sum_i += factorial(int(i))

        if sum_i == number:
            the_numbers.append(number)
    
    return sum(the_numbers)

if __name__ == '__main__':
    print(digit_factorial())