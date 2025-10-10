"""
lot of ways to check primes but if you do with simple looping it will be slow for large no.

best way sieve of eratosthenes
"""
# print all the prime no under 30

import array


n = 30

count = 0
no = 2

while no <= n:
    for i in range(1,int(no ** 0.5)+1):
        if no % i == 0:
            count += 1
            if no//i != i:
                count += 1

    if count == 2:
        print("Prime",no)
    count = 0
    no += 1

# sieve of eratosthenes

"""
we will create an empty array of lenth n
earlier populate each of them with 1 assuming every element is prime
then we know zero and one are not prime so what we will do is, we will change zero and one index as 0 non prime
Then we will find the next prime number means its values one, so we will check whether it is prime or not.
If it is prime then it's multiple cannot be a prime number, we will change the all the multiples values to 0.

"""

arr = [1] * (n+1) # creates an array of length n+1 0 to 30
arr[0] = arr[1] = 0 # the first and the zero index are now zero

for i in range(2,n+1):
    if arr[i] == 1:
        for j in range(i*i,n+1,i): # Will start the loop from i*i to get the multiples till n+1 also increment with i
            arr[j] = 0

print(arr)
for i in range(0,len(arr)):
    if arr[i] == 1:
        print("prime no :", i)
