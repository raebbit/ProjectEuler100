"""
Project Euler: Problem 48: Self powers
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

def self_powers(power, lastdigits):
    series = 0
    for n in range(1, power + 1):
        series += pow(n, n)
    
    return str(series)[-lastdigits:]

if __name__ == '__main__':
    print(self_powers(1000, 10))