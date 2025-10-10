n = 1234

i = n
count = 0
while i != 0:
    last_digit = i % 10 # mod 10 will give the last digit
    count += 1
    i //= 10 # floor divide by 10 to remove the last digit

print(count)
