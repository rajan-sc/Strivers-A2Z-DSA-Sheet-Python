"""
Problem statement:

Check if the array is sorted.

"""
# for ascending order

arr = [-1,1,-1,3,4,5]

def check_sorted_asc(arr):
    for i in range(0,len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

print(check_sorted_asc(arr))


arr = [5,5,3,2,1]

def check_sorted_desc(arr):
    for i in range(0,len(arr)-1):
        if arr[i] < arr[i+1]:
            return False
    return True

print(check_sorted_desc(arr))

# T.C = O(n)


#sorted rotated

class Solution:
    def check(self, nums: list[int]) -> bool:
        count = 0
        n = len(nums)

        for i in range(n):
            # compare each element with the next (circularly)
            if nums[i] > nums[(i + 1) % n]: #formulae to check 
                count += 1
                if count > 1:
                    return False
        return True
