"""
Problem Statement : seperate the 0 to the end and maintain the order of non zeroes.
"""

# Brute Force Approach

arr = [0,1,0,3,12]
temp = []
count = 0
for i in range(len(arr)):
    if arr[i] > 0:
        temp.append(arr[i])
    else:
        count += 1
for i in range(count):
    temp.append(0)
print(temp)

# T.C and S.C = O(n)


#Optimal Solution
"""
Approach:

In the first loop, we find the zero position and Store that position to the variable J
break as soon we find the 0

Add a check to see whether there are any zero elements or not. If we don't find any zero elements, we will directly return the array.

Then we start the second loop from j+1 to n.

If we find any non zero value we will swap that with the position j
After swap we keep increasing the position by 1. To track the position of zero.
"""

arr = [0,1,0,3,12]

def move_zeros(arr):
    j = -1
    for i in range(0,len(arr)): # step 1 find the 0 position in the array
        if arr[i] == 0:
            j = i
            break # go out as soon you find
    if j == -1:
        return arr
    for k in range(j+1, len(arr)):
        if arr[k] != 0:
            arr[k], arr[j] = arr[j], arr[k]
            j += 1
    return arr


print(move_zeros(arr))

# T.C and S.C = O(n) and O(1) space
