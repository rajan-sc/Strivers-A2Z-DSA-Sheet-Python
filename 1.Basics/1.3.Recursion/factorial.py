"""
The problem statement is to print the factorial of n.
"""
def factorial(n):
    if n <= 1:
        return n
    return n * factorial(n-1)

print(factorial(5))

# T.C = O(n) and space complexity also same.
