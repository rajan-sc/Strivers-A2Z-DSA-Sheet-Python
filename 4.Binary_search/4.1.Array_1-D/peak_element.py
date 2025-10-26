"""
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index.
If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.
In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.
"""

def findPeakElement(arr):
    n = len(arr)
    if n == 1:
        return 0
    if arr[0] > arr[1]:
        return 0
    if arr[-1] > arr[n-2]:
        return n-1

    low = 0
    high = n-2
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid+1]:
            return mid

        if arr[mid] > arr[mid - 1]:
            low = mid + 1
        else:
            high = mid - 1


arr = [1,5,1,2,1]
print(findPeakElement(arr))
