"""
Project Euler: Problem 38: Pandigital multiples
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192

192 × 2 = 384

192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. 
We will call 192384576 the concatenated product of 192 and (1, 2, 3).

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, 
giving the pandigital, 918273645, which is the concatenated product of 9 and (1, 2, 3, 4, 5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer 
with (1, 2, ... , n) where n > 1?
"""
# The product of 1,2 and 3 and (1,2,3,4,5,6), respectively, are not pandigital. 
# And the product of 4 to 9 and (1,2,3,4,5,6) are more than 9 digits.
def is_pandigital(str_num):
    if len(str_num) != 9:
        return False
    
    for i in range(1, 10):
        if str(i) not in str_num:
            return False
    
    return True

def pandigital_products(a, b, c, d):
    products = []
    for num1 in range(a, b):
        product = ''
        for i in range(c, d):
            product += str(num1 * i)

        if is_pandigital(product):
            products.append(int(product))
    
    return max(products)
    
def pandigital_multiples():
    multiples = []
    multiples.append(pandigital_products(5000, 10000, 1, 3))
    multiples.append(pandigital_products(100, 334, 1, 4))
    # multiples.append(pandigital_products(25, 34, 1, 5)) # there is no pandigital products
    multiples.append(pandigital_products(6, 10, 1, 6))

    return max(multiples)

if __name__ == '__main__':
    print(pandigital_multiples())