num = ord("A") # i know capital letter A start from 65 and how to check

n = 4

for i in range(0,n):
    for j in range(0,n-i-1):
        print(" ", end="")
    for j in range(0,i+1):
        print(chr(num+j), end="")
    for k in range(i-1,-1,-1):      #for start at -1 go till -1 so not working for first time because start not greater than stop
        print(chr(num+k), end="")
    print()

