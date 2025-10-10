"""
The problem statement is to reverse an array using two pointers and recursion.

If use a two pointer approach we don't have to create another array to store the values. We can directly swap both of the values.

Approach:
So we will start swapping from this zero index to the last index, and then move forward
We will keep going until we reach the midpoint because at the midpoint, the array is reversed.
"""

arr = [1,2,3,4,5]
start = 0
end = len(arr) - 1

def reverse(start, end, arr):
    if start > end: # base condition
        return arr
    arr[start], arr[end] = arr[end], arr[start] # Swap Elements
    return reverse(start + 1, end -1, arr) # recursion


print(reverse(start, end, arr))
