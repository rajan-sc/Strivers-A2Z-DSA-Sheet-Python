"""
Search in rotated sorted array:
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length)
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
"""

arr = [4,5,6,7,0,1,2]

def rotated_sorted(arr, k):
    target = k # for better explaination
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        # First check which half of the array is sorted
        elif arr[low] <= arr[mid]:
            if arr[low] <= target and target <= arr[mid]:
                high = mid - 1
            else:
                low = mid + 1

        else:
            if arr[mid] <= target and target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1


arr = [2,5,6,0,0,1,2]
print(rotated_sorted(arr, 3))


"""
Let's see if there are the duplicates in the array
No, my logic to find find the sorted part of the array will not work because now high low and Mid all three are the same
Solution to this is whenever I found all three same, I will just move the low one place ahead and high one place behind, and the rest can be same as is

"""
