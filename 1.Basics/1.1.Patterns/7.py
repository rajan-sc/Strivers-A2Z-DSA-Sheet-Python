n = 5
for rows in range(0,n):
    for space in range(0,n-rows):
        print(" ", end="")
    for stars in range(0,2*rows+1):
        print("*", end="")
    print()
