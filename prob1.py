"""
Problem 1:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000 (Or provided parameter value `number`.)
"""



def multiples_of3and5(number):
    def sum_of(num):
        sum_num = 0
        for i in range(0, int(number), num):
            sum_num += i
        return sum_num
    
    sum_3 = sum_of(3)
    sum_5 = sum_of(5)
    sum_15 = sum_of(15)
    return sum_3 + sum_5 - sum_15



if __name__ == '__main__':
    number = input("Insert the number: ")
    print(multiples_of3and5(number))