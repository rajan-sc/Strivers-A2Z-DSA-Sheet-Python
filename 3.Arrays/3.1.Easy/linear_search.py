"""
Problem Statement:

Given an array of integers nums and an integer target, find the smallest index (0 based indexing) where the target appears in the array.
If the target is not found in the array, return -1.
"""

arr = [1,2,3,4,5]

def linar_search(arr, k):
    for i in range(0, len(arr)):
        if arr[i] == k:
            return i
    return -1


print(linar_search(arr, 5))
