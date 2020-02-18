"""
Project Euler: Problem 32: Pandigital products

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; 
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""
def distinct_num(num1, num2, num3):
    set1, set2, set3 = set(), set(), set()
    for i in str(num1):
        set1.add(i)
    for j in str(num2):
        set2.add(j)
    for k in str(num3):
        set3.add(k)
        
    if set1 | set2 | set3 == {'1','2','3','4','5','6','7','8','9'}:
        if set1 & set2 == set() and set2 & set3 == set() and set1 & set3 == set():
            return True
        else:
            return False
    else:
        return False
        
        
# Only possible digits if multiplicand/multiplier/product: a) 1-digit x 4-digit = 4-digit  b) 2-digit x 3-digit = 4-digit
def pandigital_products():
    products = set()
    for product in range(1234, 9877):
        factor1 = 2
        while factor1 * factor1 < product:
            if product % factor1 == 0:
                factor2 = product // factor1
                if distinct_num(product, factor1, factor2) == True:
                    products.add(product)

            factor1 += 1

    return sum(products)
    

if __name__ == '__main__':
    #print(distinct_num(12, 345, 6789))
    print(pandigital_products())