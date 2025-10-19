"""
Problem statement: you have been given an array, and you have to find the second largest or smallest element without sorting.
"""


"""
# Brute Force

nums.sort() # first sort the array

largest = nums[-1]
for i in range(len(nums)-2,-1,-1): # traverse from the back and find the fist element not same as largest then break
    if nums[i] != largest:
        largest = nums[i]
        break

print(largest)

# T.C = nlogn + n (sorting + loop)

Also if no second largest will return -1
"""

# Better Approach = 2 passes of looping

nums = [13, 3, 26, 1, -1]
largest = nums[0]
for i in nums:
    if i > largest:
        largest = i
print(largest)

sec_large = -1 # considering all +ve integers if array have negative take int-min
for i in nums:
    if i > sec_large and i != largest:
        sec_large = i

print(sec_large)

# T.C = o(n + n) = O(2n)

#Optimal
def second_largest(arr):
    largest = nums[0]
    s_largest = -1 # or int_max
    for i in range(1,len(nums)):
        if nums[i] > largest:
            s_largest = largest
            largest = nums[i]
        elif arr[i] < largest and arr[i] > s_largest:
            s_largest = arr[i]
    return(largest, s_largest)


def second_smallest(arr):
    smallest = nums[0]
    s_smallest = -1 # or int_min
    for i in range(1,len(nums)):
        if nums[i] < smallest:
            s_smallest = smallest
            smallest = nums[i]

        # “If this number is bigger than the smallest but smaller than the current second smallest, update the second smallest.”
        elif arr[i] != smallest and arr[i] < s_smallest:
            s_smallest = arr[i]
    return(smallest, s_smallest)

print(second_largest(nums))
print(second_smallest(nums))


