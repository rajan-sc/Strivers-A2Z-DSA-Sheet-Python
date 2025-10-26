"""
Given a sorted array of nums and an integer x, write a program to find the lower bound of x.
The lower bound algorithm finds the first and smallest index,
in a sorted array where the value at that index is greater than or equal to a given key i.e. x.
If no such index is found, return the size of the array.
"""

# Brute

arr = [1,2,3,4,7,8,9,9,9,11]

def brute_lower(arr, k):
    for i in range(len(arr)):
        if arr[i] >= k:
            return i
    return len(arr)

print(brute_lower(arr, 6))

# T.C = O(n) and S.C = O(1)


# Optimal
"""
So first, I am finding out the Mid
And checking whether the Mid is greater than the target, if it is greater, I move the higher and low accordingly
And I will keep updating the answer to the Mid
And I will keep checking, and if I don't find their target, I can assume the target index is the length of the array
"""
def optimal_lower(arr, k):
    low = 0
    high = len(arr) -1
    ans = len(arr)
    while low <= high:
        mid = (low + high) // 2
        # maybe the answer
        if arr[mid] >= k:
            high = mid - 1 # move the search space to left
            ans = mid
        else:
            low = mid + 1 # move the search space to right
    return ans

print(optimal_lower(arr, 6))

 # t.c = O(n) and O(1) space


