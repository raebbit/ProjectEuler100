"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to n? (website: from 1 to 20?)
"""

def smallest_mult(n):
    # Find all the prime numbers smaller than n
    primes = [2]
    for i in range(3, int(n)+1, 2):
        prime = True
        for j in range(2, i):
            if i % j == 0: # not a prime number
                prime = False
        if prime:
            primes.append(i)

    # Find the biggest prime power for each prime number and multiply 
    multiple = 1
    for num in primes:
        number = num
        while number <= int(n):
            number = number * num

        number = number // num
        multiple = multiple * number

    return multiple

if __name__ == '__main__':
    n = input("Insert number n : ")
    print(smallest_mult(n))
        