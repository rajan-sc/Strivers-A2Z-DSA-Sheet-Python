"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
"""
arr = [1,1,1,1,1]

low = 0
high = len(arr) - 1
minimum = 2**30 # int_max just for comparing


while low <= high:
    mid = (low + high) // 2
# sorted may or may not have the minimum
    if arr[low] <= arr[mid]:
        minimum = min(minimum, arr[low]) # assuming the first element is minimum because of the sorted nature
        low = mid + 1 # just taking minimum and eliminating the sorted and checking in unsorted part

    else:
        minimum = min(minimum, arr[mid])
        high = mid - 1

print(minimum)


"""
For the duplicated can add a one more check mid=low=high then low + 1 and high - 1 continue
rest is same
"""
