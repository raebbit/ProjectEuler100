"""
Project Euler: Problem 16: Power digit sum
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^exponent?
"""

def power_digit_sum(exponent):
    number = 2 ** int(exponent)
    sum = 0
    for num in str(number):
        sum += int(num)
    
    return sum

if __name__ == '__main__':
    exponent = input("Exponent: ")
    print("The sum of the digits of the number 2^exponent: " + str(power_digit_sum(exponent)))