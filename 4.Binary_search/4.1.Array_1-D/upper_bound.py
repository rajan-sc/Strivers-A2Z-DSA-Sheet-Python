"""
Given a sorted array of nums and an integer x, write a program to find the upper bound of x.
The upper bound of x is defined as the smallest index i such that nums[i] > x.
If no such index is found, return the size of the array.
"""

# Brute

arr = [2,3,6,7,8,8,11,11,11,12]

def brute_lower(arr, k):
    for i in range(len(arr)):
        if arr[i] > k:
            return i
    return len(arr)

print(brute_lower(arr, 1))

# T.C = O(n) and S.C = O(1)


# Optimal
"""
So first, I am finding out the Mid
And checking whether the Mid is greater than the target, if it is greater, I move the higher and low accordingly
And I will keep updating the answer to the Mid
And I will keep checking, and if I don't find their target, I can assume the target index is the length of the array
"""
def upper_bound_optimal(arr, k):
    low = 0
    high = len(arr) -1
    ans = len(arr)
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] > k:
            high = mid - 1
            ans = mid
        else:
            low = mid + 1
    return ans

print(upper_bound_optimal(arr, 2))

 # t.c = O(n) and O(1) space
