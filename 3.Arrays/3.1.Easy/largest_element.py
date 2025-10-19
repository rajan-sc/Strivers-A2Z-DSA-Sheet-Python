"""
Problem statement: you have been given an array, and you have to find the largest element.

Brute force: first we will sort the array ang get the last/ first index acc to sort.
"""
nums = [3, 3, 6, 1, -1]

largest = nums[0]
for i in nums:
    if i > largest:
        largest = i

print(largest)

# T.C = O(n)

