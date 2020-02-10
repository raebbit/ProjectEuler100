"""
Project Euler: Problem 23: Non-abundant sums
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 
the smallest number that can be written as the sum of two abundant numbers is 24. 

By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be 
expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all positive integers <= n which cannot be written as the sum of two abundant numbers.
"""

import time # Because there is an one-minute rule
import math

def sum_nonabundant_numbers(n):
    # Find all abundant numbers less than n : 1st step
    abundants = []
    for num in range(12, int(n)):
        i = 2
        sum_divisors = 1
        while i <= (math.sqrt(num)): # it really reduced the execution time
            if num % i == 0:
                if num // i == i:
                    sum_divisors += i
                else:
                    sum_divisors += i
                    sum_divisors += num // i
            i += 1

        if sum_divisors > num:
            abundants.append(num)
    
    time1 = time.time()
    print("1st step time: {}".format(time1 - start_time))

    # the sum of two abundant numbers : 2nd step
    sums_two_abundant = set()
    dupe_abundants = abundants
    for k in abundants:
        for j in dupe_abundants:
            h = k + j
            if h < int(n):
                sums_two_abundant.add(h)
            else: 
                pass
        
        del dupe_abundants[:0]
        
    time2 = time.time()
    print("2nd step time: {}".format(time2 - time1))

    # the sum of all positive integers <= n which cannot be written as the sum of two abundant numbers : last step
    answer = 0
    for m in range(1, int(n)):
        if m not in sums_two_abundant:
            answer += m
    
    time3 = time.time()
    print("last step time: {}".format(time3 - time2))
    return answer

        
if __name__ == '__main__':
    n = input("n : ")
    start_time = time.time()
    print("The answer: " + str(sum_nonabundant_numbers(n)))
    end_time = time.time()
    print("Total execution time: {}".format(end_time - start_time))
    
    
    
    