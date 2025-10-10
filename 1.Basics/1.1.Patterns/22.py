n = 4
"""
This question is something
you have to do obersvation as any other
here we have to find the top bottom left right distance from the specific value
"""
for i in range(0, 2*n-1):
    for j in range(0, 2*n-1):
        top = i
        bottom = (2*n - 2) - i # subtracting the last index and i to get the distance from bottom
        right = (2*n - 2) - j
        left = j
        print(n - min(min(top, bottom), min(left,right)), end="") 
    print()


