n = 14
half = n//2
for i in range(0,n):
    if i < half:
        stars_a = half - i
        spaces = 2 * i
        stars_b = half - i
    else:
        stars_a =   i - half + 1 # here i - half  is same as starting from 0
        spaces = n - 2 - (2 *(i - half))
        stars_b = i - half + 1
    print("*" * stars_a + " " * spaces + "*" * stars_b)


# i can also unify both stars_a and b
