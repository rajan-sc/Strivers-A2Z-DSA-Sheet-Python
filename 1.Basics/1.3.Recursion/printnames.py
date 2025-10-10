"""
Problem: Print your Name N times using recursion

How to write recursions?
So we have to tell what our function does, and then write the recursive call of what will happen next, just like the for loop
also we have to write a stopping condition.

"""



n = 5
def print_name(a):
    if a <= 0: # Stopping Condition
        return
    print("hello", a)
    print_name(a-1)     # Recursive Call


print_name(5)
