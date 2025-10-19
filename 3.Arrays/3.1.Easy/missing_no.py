"""
Problem statement:

Given an array arr containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.
and only 1 is missing.
"""


arr = [0,1,3]

n = len(arr)

max_element = arr[-1]
for i in arr:
    if i > max_element:
        max_element = i

# brute
def brute_missing(arr):
    for i in range(0, max_element):
        if i not in arr:
            print(i)

# T.C = o(n**2) space is O(1)

#better solution
def missing_elements(arr):
    n = len(arr)

    # finding max_element
    max_element = arr[-1]
    for i in arr:
        if i > max_element:
            max_element = i

    if max_element == n: # logic for handling range
        max_element += 1
    elif max_element + 1 == n:
        max_element += 2

    temp = [0] * (max_element)

    # mark the existing element in the map
    for i in arr:
        temp[i] += 1

    # fetching the found value (printing missing)
    for i in range(len(temp)):
        if temp[i] == 0:
            print(i)

missing_elements(arr)

# t.c = O(n + max)
# space = O(n)


"""
Optimal Solution
"""
# you can use xor to find the missing element

# sum of the n natural no. where n is the max element  - sum of array

def n_missing_optimal(arr):
    n = len(arr)

    # finding max_element
    max_element = arr[-1]
    for i in arr:
        if i > max_element:
            max_element = i
    if n == max_element +1:
        max_element += 1
    arr_total = 0
    for i in arr:
        arr_total += i

    sum_natural_no = (max_element * (max_element + 1)) // 2

    print(sum_natural_no - arr_total)

arr = [0,1,3]
n_missing_optimal(arr)

# T.C = O(n) and space O(1)


def xor_missing_optimal(arr):
    n = len(arr)

    # finding max_element
    max_element = arr[-1]
    for i in arr:
        if i > max_element:
            max_element = i
    if n == max_element +1:
        max_element += 1

    xor1 = 0
    for i in range(0,max_element+1):
        xor1 ^= i

    xor2 = 0
    for j in arr:
        xor2 ^= j

    print(xor1 ^ xor2)

arr = [0,1,2,3]
xor_missing_optimal(arr)

"""
xor is better than addition because it is fast at CPU level
xor also prevents overflow because xor only Flip the bits
"""
