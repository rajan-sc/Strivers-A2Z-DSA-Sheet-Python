"""
First and last occurance of x

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""

# Brute

arr = [2,4,6,8,8,8,11,13]

def brute_first_last(arr, k):
    first = -1
    last = -1
    for i in range(len(arr)):
        if first == -1 and arr[i] == k:
            first = i
            last = i
        if arr[i] == k:
            last = i
    return first, last

print(brute_first_last(arr, 13))

# T.C = O(n)

from typing import List

class Solution:
    def element_search(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        first = -1
        last = -1

        # ---- Find first occurrence (lower bound) ----
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                first = mid
                high = mid - 1  # keep going left
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        # ---- Find last occurrence (upper bound) ----
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                last = mid
                low = mid + 1  # keep going right
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return [first, last]


def optimal_first_last(arr, k):
    low, high = 0, len(arr) - 1
    first = len(arr)
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= k:
            high = mid - 1
            first = mid
        else:
            low = mid + 1

    low, high = 0, len(arr) - 1
    last = len(arr)
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > k:
            high = mid - 1
            last = mid - 1
        else:
            low = mid + 1

    if first >= len(arr) or arr[first] != k:
        first = -1
    if last >= len(arr):
        last = last - 1

    return first, last

arr = [1,1,1,1]
print(optimal_first_last(arr, 1))
