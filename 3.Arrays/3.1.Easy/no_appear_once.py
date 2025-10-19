"""
Given a non-empty array of integers arr, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""
arr = [1,1,3,4,4]

# brute
for i in range(0,len(arr)):
    num = arr[i]
    count = 0
    for j in range(0,len(arr)):
        if arr[j] == num:
            count += 1
    if count == 1:
        print(arr[i])
        break

# t.c = O(n**2) and space O(1)

# better


arr = [1,1,3,4,4]
d = {}

for i in arr:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

for key in d:
    if d[key] == 1:
        print(key)

"""
Time = O(n)
	•	In Python, dictionaries are implemented as hash tables.
	•	Average time complexity for key lookup, insertion, and update is O(1).
	•	Worst-case (rare, due to hash collisions) can be O(n), but in practice, Python dicts are amortized O(1).

    Explain each complexity and how you got that
"""


# optimal

arr = [1,1,3,4,4]

def single_appear(arr):
    xor = 0
    for i in arr:
        xor = xor ^ i
    print(xor)

single_appear(arr)
