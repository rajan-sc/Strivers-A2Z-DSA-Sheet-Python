"""
lcm = (a * b)/gcd(a,b)
"""
a = 12
b = 9

def gcd(a,b):
    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    if a == 0:
        return b
    else:
        return a


lcm = (a * b)//gcd(a,b)
print(lcm)





