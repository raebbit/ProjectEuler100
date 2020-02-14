"""
Project Euler: Problem 30: Digit n powers
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4

8208 = 8^4 + 2^4 + 0^4 + 8^4

9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of n powers of their digits.
"""

def digit_n_powers(n):
    answer = 0
    i = 0
    min_range, max_range = 0, 0
    while i < int(n):
        min_range += 2 ** int(n)
        max_range += 9 ** int(n)     # The ranges are not mathmethically confirmed. It's just my hunch.
        i += 1                       # However, it works when n is 2 to 5. maybe 6 too?

    for number in range(min_range, max_range):
        sum_pow_digits = 0
        for num in str(number):
            sum_pow_digits += int(num) ** int(n)
        if number == sum_pow_digits:
            answer += number
        else:
            continue
    
    return answer

if __name__ == '__main__':
    n = input("n? : ")
    print(digit_n_powers(n))