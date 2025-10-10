"""
The problem statement is to print the sum of first and natural numbers using recursion.
Also, there is a formula for some of our natural numbers. (n * (n+1))/2
"""

def n_natural(n):
    if n <= 1:
        return n
    return n + n_natural(n-1)

print(n_natural(3))

# T.C = O(n)
