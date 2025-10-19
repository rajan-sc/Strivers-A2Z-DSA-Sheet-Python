"""
Problem statement: so we have to rearrange the list or an array in an ascending order

We can solve this problem by using the various sorting technique, but here we are using selection sort

How does selection short works?
First, we have to find the minimum value, then we will swap that value to the first place that is the zero index
Then we find the next minimum number, and then we swap that with the first index, we start at first index because before first index the list is sorted.

Logic:

Divide array into 2 parts:

Left side → already sorted

Right side → unsorted

Each iteration picks the smallest element from the unsorted part
and places it at the correct position (i).
"""

# arr = [86,23,45,56,23,96,12]
arr = [-1,-2,0,2,-5]

n = len(arr)

for i in range(0,n):
    min_index = i # we have assume here that i is the smallest value
    for j in range(i+1,n):
        if arr[j] < arr[min_index]: # checking the min with the next value (range-loop)
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]


print(arr)

# Runs in O(n²) time, O(1) space.
