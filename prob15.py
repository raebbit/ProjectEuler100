"""
Project Euler: Problem 15: Lattice paths
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

a diagram of 6 2 by 2 grids showing all the routes to the bottom right corner.

How many such routes are there through a given gridSize?
"""

import math 

def lattice_paths(gridsize):
    # Since it's always n by n grid
    n = int(gridsize)
    return math.factorial(2 * n) // (math.factorial(n)) ** 2


if __name__ == '__main__':
    gridsize = input("Grid Size: ")
    print(lattice_paths(gridsize))

