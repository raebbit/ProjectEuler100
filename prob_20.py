"""
Project Euler: Problem 20: Factorial digit sum
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits n!
"""
# I won't use 'import math' to calculate factorial this time.
def factorial_digit_sum(n):
    # Factorial 
    factorial = 1
    for i in range(2, int(n)+1):
        factorial *= i

    # Digit sum
    digit_sum = 0
    for num in str(factorial):
        digit_sum += int(num)

    return digit_sum

if __name__ == '__main__':
    n = input("Insert the number n: ")
    print("The sum of the digits n!: " + str(factorial_digit_sum(n)))