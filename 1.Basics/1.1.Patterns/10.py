n = 5

for i in range(2 * n - 1):
    if i < n:
        stars = 1 + i
    else:
        stars = 2*n - i - 1
    print("*" * stars)
