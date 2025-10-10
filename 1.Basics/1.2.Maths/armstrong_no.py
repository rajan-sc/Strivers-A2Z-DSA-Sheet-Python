"""
sum of cubes of no. is called as armstromg no.
example :
153
1 + 125 + 27 = 153
"""

n = 153

i = n
rev = 0
while i != 0:
    last_digit = i % 10 # mod 10 will give the last digit
    rev += last_digit ** 3 # cube of last digit and adding
    i //= 10 # floor divide by 10 to remove the last digit

if rev == n:
    print("Yes")
else:
    print("No")
