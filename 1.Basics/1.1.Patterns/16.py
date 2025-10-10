num = ord("A") # i know capital letter A start from 65 and how to check

n = 5

for i in range(0,n):
    for j in range(0,i+1):
        print(chr(num+i), end="")
    print()

