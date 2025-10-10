n = 4

i = 2
a = 0
b = 1

for j in range(0, n+1):
    while i <= j:
        a, b = b, a + b
        i += 1
    print(j, a)


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(4))


# time complexity = O(2^n) and space complexity = O(n) (due to call stack depth).

"""
                   fib(4)
                /           \
           fib(3)             fib(2)
          /      \            /     \
     fib(2)     fib(1)   fib(1)    fib(0)
     /    \
 fib(1)  fib(0)

=>
                   3
                /     \
              2         1
            /   \      / \
           1     1    1   0


"""


