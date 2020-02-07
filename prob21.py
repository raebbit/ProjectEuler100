"""
Project Euler: Problem 21: Amicable numbers (친화수)
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).

If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under n.
"""

def divisor_sum(number):
    d_sum = 0
    for i in range(1, number):
        if number % i == 0:
            d_sum += i
    
    return d_sum 

def sum_amicable_num(n):
    amicables = []
    for num in range(2, int(n)):
        if num not in amicables:
            d_num = divisor_sum(num)
        
            if d_num != num and divisor_sum(d_num) == num:
                amicables += [d_num, num]
    
    print(amicables)
    return sum(amicables)

if __name__ == '__main__':
    n = input("n : ")
    print(sum_amicable_num(n))