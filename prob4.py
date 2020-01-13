"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two n-digit numbers.(website: two 3-digit numbers)
"""

def isit_palindrome(number):
    # It's for even-length palindrome only
    number = str(number)
    for i in range(len(number)//2):
        j = len(number) - i - 1
        
        if number[i] == number[j]:
            continue
        else:
            return False
    
    return True



def largest_palindrome(n):
    box = []
    # Since I only need to find the largest, I set the range of a,b to the last 10**(n-1) numbers of the n -digits
    # I think we could find the largest palindrome of the product of two n-digit in the range below (no pf yet)
    for a in range(9*10**(int(n)-1), 10**int(n)):  
        for b in range(9*10**(int(n)-1), 10**int(n)): 
            product = a * b

            # check if the product is palindrome
            if isit_palindrome(product):
                box.append(product)

    return max(box)
            

if __name__ == '__main__':
    n = input("Set the size of divisors of palindrome: ")
    print("Largest Palindrome of two " + n + "-digit numbers: " + str(largest_palindrome(n)))

