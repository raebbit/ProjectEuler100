"""
Project Euler: Problem 50: Consecutive prime sum
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

def is_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def consecutive_prime_sum(limit):
    primes = [2, 3]
    for k in range(1, (int(limit)//6) + 1):
        for i in [-1, 1]:
            n = 6 * k + i
            if is_prime(n):
                primes.append(n)
            
    count, max_count = 0, 1
    s = 0
    while s < len(primes) - 1:
        sum_primes = sum(primes[s : s + max_count])
        count = max_count - 1
        while sum_primes <= int(limit):
            count += 1
            sum_primes = sum(primes[s : s + count])
        
            if sum_primes in primes:
                max_count = count
                max_sum = sum_primes
        
        s += 1

    return max_sum, max_count



if __name__ == "__main__":
    limit = input("Limit : ")
    print(consecutive_prime_sum(limit))