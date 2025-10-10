n = 1234

i = n
rev = 0
while i != 0:
    last_digit = i % 10 # mod 10 will give the last digit
    rev = rev * 10 + last_digit
    i //= 10 # floor divide by 10 to remove the last digit

if rev == n:
    print("Yes")
else:
    print("No")
