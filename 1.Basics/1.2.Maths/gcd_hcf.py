# Find what is the greatest common divisor of two numbers
"""
Euclidian Algorith
gcd(a,b) = gcd(a-b,b) where a > b
= (greater % smaller, smaller) keep doing till one becomes 0
and the other remaining is your gcd
"""
a = 12
b = 9

while a > 0 and b > 0:
    if a > b:
       a = a % b
    else:
        b = b % a
if a == 0:
    print(b)
else:
    print(a)

