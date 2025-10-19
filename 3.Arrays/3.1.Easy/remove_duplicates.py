"""
Problem statement : you have to remove the duplicates in place in a given sorted array.
"""

from pprint import pprint


arr = [1,2,2,4,4,5,5]

# brute force
# traverse list and add each element to the set
# now, write an another loop to add the elements back to the list. from len(set) index(0,len(set)) and update the elements
# temp_set = set()
# x = 0
# for i in range(len(arr)):
#     if arr[i] not in temp_set:
#         temp_set.add(arr[i])
#         arr[x] = arr[i]
#         x += 1

# print(x, arr)

"""
# t.c ⚠️ Worst Case

Worst case happens if hash collisions occur in the set.

In theory, arr[i] not in temp_set can degrade to O(n) per check (if all elements hash to same bucket).

Then the total worst-case complexity → O(n²).

"""


# Optimal solution (in place pointer swap)
def remove_duplicates(arr):
    i = 0
    for j in range(1,len(arr)):
        if arr[j] != arr[i]:
            arr[i+1] = arr[j]
            i += 1
    return(i + 1, arr)

print(remove_duplicates(arr))

# T.C = O(n)

