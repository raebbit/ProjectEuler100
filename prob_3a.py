"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the given number? (fCC)
(Website: What is the largest prime factor of the number 600851475143 ?)
"""
# I was stuck on thought that I have to put all the divisors in one list
# So when this code compute the number 600851475143, it takes forever!! 
# not a good method, but I learned how to use boolean value to check if it's prime number or not
def largest_primefactor(n):
    numbers = []

    # Is it a factor of n?
    for j in range(2, int(n)+1):
        if int(n) % j == 0:
            numbers.append(j)

    # prime numbers less than n
    prime_fac = []
    for num in numbers:
        prime = True   # Using Boolean 
        for i in range(2, num):
            if num % i == 0:  # not a prime number
                prime = False
        if prime:
            prime_fac.append(num)
        
    # the largest prime factor
    return max(prime_fac)

if __name__ == '__main__':
    n = input("Insert the number bigger than 1: ")
    print("The Largest Prime Factor: " + str(largest_primefactor(n)))
