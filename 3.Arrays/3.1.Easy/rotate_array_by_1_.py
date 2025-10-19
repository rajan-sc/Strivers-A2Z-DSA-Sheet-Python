"""
Problem Statement:
Rotate the array left by 1 places.
"""

arr = [1,2,3,4,5]

def rotate_array_left(arr):
    temp = arr[0]
    for i in range(1, len(arr)):
       arr[i-1] = arr[i]
    arr[-1] = temp
    return arr

print(rotate_array_left(arr))
# T.C = 0(n) and space is O(n) bescause array space (already created)
# auxilary space = O(1)

def rotate_array_right(arr):
    temp = arr[-1]                     # store last element
    for i in range(len(arr)-1, 0, -1): # move elements one step right
        arr[i] = arr[i-1]
    arr[0] = temp                      # put last element at front
    return arr

arr = [1, 2, 3, 4, 5]
print(rotate_array_right(arr))
