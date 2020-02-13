"""
Project Euler: Problem 28: Number spiral diagonals
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25

20  7  8  9 10

19  6  1  2 11

18  5  4  3 12

17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a n by n spiral formed in the same way?
"""
# 1 (1x1)
# 3 5 7 9 (vertices of 3x3, d=2) ---> first sequence *d is common difference
# 13 17 21 25 (vertices of 5x5, d=4)
# 31 37 43 49 (vertices of 7x7, d=6)
# The first terms of each sequences (1, 3, 13, 31, ...) are progression of difference(계차수열).

def spiral_diagonals(n):
    k = (int(n) - 1) // 2  # kth sequence/ Since n from n by n spirals are odd numbers.
    sum_spiral = 1 
    for i in range(1, k+1):
        a1 = 4*i*i - 2*i + 1 # general formula of progression of difference
        j = 1
        d = 2 * i
        while j < 5:
            sum_spiral += a1
            a1 += d
            j += 1

    return sum_spiral   

if __name__ == '__main__':
    n = input("n? (n by n, n must be an odd number): ")
    print(spiral_diagonals(n))