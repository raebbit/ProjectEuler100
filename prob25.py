"""
Project Euler: Problem 25: 1000-digit Fibonacci number
The Fibonacci sequence is defined by the recurrence relation:

F_n = F_(n−1) + F_(n−2), where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain n digits?
"""

def digit_fibonacci(n):
    a, b = 1, 1
    c = 0
    index = 2
    while len(str(c)) < int(n):
        c = a + b
        index += 1

        a = b
        b = c
        
    return index

if __name__ == '__main__':
    n = input("n digits? : ")
    print(digit_fibonacci(n))
    

