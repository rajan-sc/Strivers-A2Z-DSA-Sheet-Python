"""
Problem Statement : rotate the array by k places
"""
# brute force
def rotate_array(arr, k):
    k = k % len(arr)
    for loop in range(0,k):
        first = arr[0]
        for i in range(1, len(arr)):
            arr[i-1] = arr[i]
        arr[-1] = first
    return arr
arr = [1,2,3,4,5]
print(rotate_array(arr, 1)) # rotate by 3 places left


def rotate_array_right(arr, k):
    n = len(arr)
    k = k % n  # handle cases where k > n
    for _ in range(k):
        last = arr[-1]  # store last element
        for i in range(n - 2, -1, -1):  # shift right
            arr[i + 1] = arr[i]
        arr[0] = last
    return arr

arr = [1, 2, 3, 4, 5]
print(rotate_array_right(arr, 1))
# t.c = O(k x n)


"""
Optimal :
"""
arr = [1,2,3,4,5]
k = 3

def rotate_array_k(arr, k):

    def reverse(s, e):
        while s < e:
            arr[s], arr[e] = arr[e], arr[s]
            s += 1
            e -= 1
        return arr

    n = len(arr)
    k = k % n # handles k > n

    reverse(0, k-1) # reverse k elements
    reverse(k , n-1) # reverse k remaining
    return reverse(0, n-1) # reverse whloe array


print(rotate_array_k(arr, k))

# T.C = O(n)
# S.C = O(1)


# right shift leetcode 189

def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    def reverse(s,e):
        while s < e:
            nums[s], nums[e] = nums[e], nums[s]
            s += 1
            e -= 1
        return nums

    n = len(nums)
    k = k % n

    reverse(n-k, n-1)
    reverse(0, n-k-1)
    reverse(0, n-1)
    return nums

