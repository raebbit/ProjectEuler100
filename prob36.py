"""
Project Euler: Problem 36: Double-base palindromes

The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than n, whereas 1000 <= n <= 1000000, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""
def binary_expression(number):
    # from base 10 to base 2
    binary = 0
    while number > 0:
        n = 0
        while pow(2, n) <= number:
            n += 1
        else:
            if n == 0:
                binary += 1
                number -= 1
            else:
                binary += pow(10, n-1)
                number -= pow(2, n-1)
    
    return binary

def is_palindrome(number):
    num = str(number)
    if len(num) % 2 == 1:
        half = (len(num) - 1) // 2
    else:
        half = len(num) // 2

    for i in range(half):
        if num[i] != num[-i-1]:
            return False
    
    return True

def double_base_palindromes(n):
    sum_palindromes = 0
    for k in range(1, int(n)):
        if is_palindrome(k):
            k_binary = binary_expression(k)
            if is_palindrome(k_binary):
                sum_palindromes += k
        
    return sum_palindromes

if __name__ == '__main__':
    #print(binary_expression(4))
    #print(is_palindrome(584))
    n = input("n ? : ")
    print(double_base_palindromes(n))
        