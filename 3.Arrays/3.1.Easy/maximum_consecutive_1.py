"""
Problem Statement :
Given a binary array nums, return the maximum number of consecutive 1's in the array.
"""

arr = [1,1,1,1,0,1,1,1]
n = len(arr)
count = 0
max_i = 0

for i in arr:
    if i == 1:
        count += 1
        max_i = max(count, max_i)
    else:
        count = 0

print(max_i)


