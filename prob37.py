"""
Project Euler: Problem 37: Truncatable primes (절단 가능 소수)
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, 
and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only n (8 <= n <= 11) primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
def is_prime(number):
    if int(number) == 1:
        return False
     
    i = 2
    while i * i <= int(number):
        if int(number) % i == 0:
            return False
        i += 1
        
    return True

def truncatable_primes(n):
    truncatables = []
    number = 23 
    while len(truncatables) < int(n):
        is_truncatable = True
        if is_prime(number):
            for i in range(1, len(str(number))):
                if is_prime(str(number)[i:]) == False:
                    is_truncatable = False
                    break
                elif is_prime(str(number)[:i]) == False:
                    is_truncatable = False
                    break

            if is_truncatable == True:
                # print(number)
                truncatables.append(number)
        
        number += 2
    
    return sum(truncatables)

if __name__ == '__main__':
    n = input("n? : ")
    print(truncatable_primes(n))