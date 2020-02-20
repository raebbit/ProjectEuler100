"""
Project Euler: Problem 35: Circular primes
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below n, whereas 100 <= n <= 1000000?

Note:
Circular primes individual rotation can exceed `n`.
"""
def is_prime(num):
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False

        i += 1

    return True

def is_all_odd(str_num):
    for num in str_num:
        if int(num) % 2 == 0:
            return False
        
    return True
    
def circular_primes(n):
    count = 2 # 2, 3
    for k in [1, -1]:
        for h in range(6, int(n), 6):
            number = k + h
            is_circular_number = True
            if is_prime(number) and is_all_odd(str(number)): # Every digit must be an odd number
                for i in range(1, len(str(number))):
                    cir_number = str(number)[i:] + str(number)[:i]
                
                    if is_prime(int(cir_number)) == False:
                        is_circular_number = False
        
                if is_circular_number == True:
                    count += 1

    return count


if __name__ == '__main__':
    n = input("n ? : ")
    print("The number of circular primes below n: " + str(circular_primes(n)))



