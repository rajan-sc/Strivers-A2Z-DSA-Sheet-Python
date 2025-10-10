n = 30


"""
All the divisors come in pairs.
if 1 is a factor of 30 so 30 will also be the factor of 1
and so on
"""

for i in range(1,int(n ** 0.5)+1): # looping till sqrt n will get all the divisors
    if n % i == 0:
        print(i)
        if n/i != i: # getting all the divisor pairs and also edge case to not get the divisor which will come in pair
            print(n//i)
