"""
Floor and Ceil in Sorted Array

Given a sorted array nums and an integer x.
Find the floor and ceil of x in nums.
The floor of x is the largest element in the array which is smaller than or equal to x.
The ceiling of x is the smallest element in the array greater than or equal to x.
If no floor or ceil exists, output -1.
"""

arr = [2,4,6,8,8,8,11,13]


def floor_ceil(arr, k):
    low = 0
    high = len(arr) - 1
    ans_floor = -1
    ans_ceil = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == k:
            # exact match → both floor and ceil are k
            return k, k

        elif arr[mid] < k:
            low = mid + 1
            ans_floor = arr[mid]

        else:
            high = mid - 1
            ans_ceil = arr[mid]

    return ans_floor, ans_ceil


print(floor_ceil(arr, 8))
