n = 9
half = n//2
for i in range(0,n):
    if i < half+1:
        stars = i+1
        space = 2*(half-i)
    else :
        stars = half - (i - half -1) # here (i - half -1) is i for me i am starting i from 0-3
        space = 2 *(i - half -1) + 2

    print("*" * stars + " " * space + "*" * stars)
