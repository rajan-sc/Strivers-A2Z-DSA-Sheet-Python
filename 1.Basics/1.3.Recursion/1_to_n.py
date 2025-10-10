"""
Problem statement is to print the numbers from one to N using recursion.

Also need to learn how the recursive works in the call stack, so it works like first in last out.
"""



def print_n_no(a):
    if a <= 0:
        return

    print_n_no(a-1) # recursive call
    print(a)

print_n_no(5)

