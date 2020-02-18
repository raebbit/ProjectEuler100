"""
Project Euler: Problem 31: Coin sums
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can n pence be made using any number of coins?
"""
# "This is a typical problem that demonstrates the use of partitions which can be solved by using dynamic programming"
#  The basic idea is recursive. 

def coin_sums(n):
    target = int(n)
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    counts = [1] + [0] * target

    for coin in coins:
        for i in range(coin, target+1):
            counts[i] += counts[i - coin]
                                
    return counts[target]


if __name__ == '__main__':
    n = input("How much in pence? : ")
    print(coin_sums(n))
