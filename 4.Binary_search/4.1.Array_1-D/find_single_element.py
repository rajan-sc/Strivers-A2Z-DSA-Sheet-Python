"""
Single element in sorted array

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.
"""

from math import sin


nums = [1,1,2,3,3,4,4,8,8]

"""
(even, odd) = i am on left half
element is on right half will eliminate the left half
"""



def single_element(nums):

    n = len(nums)
    low = 1
    high = n-2
    if len(nums) == 1:
            return nums[0]
    if nums[0] != nums[1]:
        return nums[0]
    if nums[n-1] != nums[n-2]:
        return nums[n-1]

    while low <= high:

        mid = (low + high) // 2
        if nums[mid] != nums[mid+1] and nums[mid] != nums[mid-1]:
            return nums[mid]
        # by observation checking where i am on
        if ((mid % 2 == 1 and nums[mid] == nums[mid -1]) or (mid % 2 == 0 and nums[mid] == nums[mid + 1])):
             low = mid + 1 # eliminating the left half
        else:
             high = mid - 1


print(single_element(nums))








