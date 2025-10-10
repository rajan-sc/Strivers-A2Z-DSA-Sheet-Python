n = 5
for rows in range(0,n):
    for space in range(0,n-rows):
        print(" ", end="")
    for stars in range(0,2*rows+1):
        print("*", end="")
    print()
for rows in range(0,n):
    for space in range(0,rows+1):
        print(" ", end="")
    for stars in range(0,2*(n-rows)-1):
        print("*", end="")
    print()


n = 5

for i in range(2 * n - 1):
    if i < n:
        stars = 1 + i * 2
        spaces = n - i
    else:
        stars = 1 + (2*n - i - 2) * 2
        spaces = i - n + 2
    print(" " * spaces + "*" * stars)
