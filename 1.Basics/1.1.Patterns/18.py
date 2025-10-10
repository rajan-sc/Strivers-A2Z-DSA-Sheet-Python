n = 5
num = 65 # "A"
for i in range(0,n):
    for j in range(n - i - 1, n, 1):
        print(chr(j+num), end="")
    print()

