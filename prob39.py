"""
Project Euler: Problem 39: Integer right triangles
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ n, is the number of solutions maximised?
"""
def is_right_triangle(x, y, z):
    if x*x + y*y == z*z:
        return True
    else:
        return False


def integer_right_triangle(n):
    max_sol_p = 12
    max_count = 1
    for p in range(12, int(n)+1): # The smallest integer right triangle is {3,4,5}.
        count = 0  
        for a in range(1, (p//3)+1):
            for b in range(a, (p//2)+1):
                c = p - a -b
                
                if is_right_triangle(a, b, c):
                    count += 1
        
        if count > max_count:
            max_count = count
            max_sol_p = p

    return max_sol_p


if __name__ == '__main__':
    n = input("n ? : ")
    print(integer_right_triangle(n))