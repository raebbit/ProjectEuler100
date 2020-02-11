"""
Project Euler: Problem 24: Lexicographic permutations

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210
What is the nth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
import math

def lexicographic_permutations(n):
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    answer = ''
    num = int(n)
    i = 9
    while i > 2:
        if num == math.factorial(i): # then index should be 0
            answer += numbers[0]
            del numbers[0]
        else:
            index = num // math.factorial(i) # quotient
            num = num % math.factorial(i) # remainder

            answer += numbers[index]
            del numbers[index]

        i -= 1
        
    # last three numbers
    if num % 2 == 0:
        index = (num - 2) // 2
        answer += numbers[index]
        del numbers[index]
        answer += numbers[1] + numbers[0]
    else:
        index = (num - 1) // 2
        answer += numbers[index]
        del numbers[index]
        answer += numbers[0] + numbers[1]
    return answer
            
     
if __name__ == '__main__':
    n = input("n? : ")
    print(lexicographic_permutations(n))