"""
Problem Statement:

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums.
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""

arr = [3, 0, 6, 7, 9, 12, 16, 17]
target = 0

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    print("loop start")

    while low <= high:
        mid = (low + high) // 2  # <-- move mid here (update each loop)

        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1  # not found

print(binary_search(arr, target))

# Time: O(log n) — halves the search space each step
# Space: O(1) — only uses a few variables
