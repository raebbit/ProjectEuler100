"""
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first n natural numbers and the square of the sum. (website n = 100)
"""

# using sum formula 
def sum_square_difference(n):
    num = int(n)
    sum_of_squares = (num*(num + 1) //2) ** 2
    square_of_sum = num * (num + 1) * (2*num + 1) // 6

    return sum_of_squares - square_of_sum

if __name__ == '__main__':
    n = input("n ? : ")
    print(sum_square_difference(n))