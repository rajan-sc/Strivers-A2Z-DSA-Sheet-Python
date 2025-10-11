"""
The problem statement is to find the occurrence of an element in an array.
Without hashing, we can do it by looping through the array and assigning counter to it, and an additional while loop, if the size of the array is very large, it will take a huge amount of time.
We can solve this problem by using a hash map
In the hash map, we do pre-computation and almost similar to sieve of eratosthenes
At the time of fetching we will find the no and count directly from the hash
"""

arr = [1,1,2,4,5,6,9,6,3,5]
length_arr = len(arr) # find the length of array

temp = [0] * (length_arr) # creates an array 0-9

for i in arr: # if found i in arr increase 1 at index i in temp
    temp[i] += 1

print(temp)

# T.C = O(n) and S.C = O(n)


max_freq = max(temp)

# indices (numbers) having that max frequency
max_elements = [i for i in range(len(temp)) if temp[i] == max_freq] # list comprehension to create new list with values which have max. freq

print("Elements with max frequency:", max_elements)
print("Max frequency:", max_freq)






"""
Also can use dictionary save space
"""


arr = [1,1,2,4,5,6,9,6,3,5]

dicnry = {}   # empty dictionary

for i in arr:
    if i in dicnry:
        dicnry[i] += 1
    else:
        dicnry[i] = 1

print(dicnry.items())

max_freq = max(dicnry.values())

max_elements = [key for key, val in dicnry.items() if val == max_freq]

print("Elements with max frequency:", max_elements)
print("Max frequency:", max_freq)
