# Recursion in Python

Recursion is a programming technique where a function **calls itself** to solve smaller instances of the same problem. It is often used for problems that can be divided into similar subproblems.

How to write recursions?
So we have to tell what our function does, and then write the recursive call of what will happen next, just like the for loop
also we have to write a stopping condition.

---

## Key Components of Recursion

1. **Base Case (Stopping Condition)**
   - Prevents infinite recursion
   - Defines the simplest version of the problem

2. **Recursive Call**
   - Calls the same function with a smaller/simpler input

3. **Combine Result**
   - Uses the result of the recursive call to build the solution

---

## Example 1: Factorial of a Number

Factorial of `n` is `n * (n-1) * ... * 1`

```python
def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    return n * factorial(n - 1)  # Recursive call

print(factorial(5))  # Output: 120
