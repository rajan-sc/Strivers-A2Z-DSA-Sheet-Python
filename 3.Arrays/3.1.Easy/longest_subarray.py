"""
Longest subarray with sum K

Given an array nums of size n and an integer k, find the length of the longest sub-array that sums to k. If no such sub-array exists, return 0.


Examples:
Input: nums = [10, 5, 2, 7, 1, 9],  k=15

Output: 4

Explanation:

Contigious part inside the array
The longest sub-array with a sum equal to 15 is [5, 2, 7, 1], which has a length of 4.
This sub-array starts at index 1 and ends at index 4, and the sum of its elements (5 + 2 + 7 + 1) equals 15.
Therefore, the length of this sub-array is 4.
"""

# Brute approach

# will use 3 loops for the subarray

arr = [10, 5, 2, 7, 1, 9]
n = len(arr)
maxi = 0
for i in range(0, n):
    for j in range(i,n):
        sum = 0
        for k in range(i,j+1):
            sum += arr[k]
        if sum == 10:
            maxi = max(maxi, j-i+1)
print(maxi)
# Time complexity is O(n^3) and space is O(1)


# brute optimized

arr = [10, 5, 2, 7, 1, 9]
max_sum = 0
for i in range(0, len(arr)):
    sum = 0
    for j in range(i, len(arr)):
        sum += arr[j]
        if sum == 10:
            max_sum = max(max_sum, j - i + 1)
print(max_sum)

# Time complexity is O(n^2) and space is O(1)





# BETTER SOLUTION
"""

“I used a prefix-sum approach with a hashmap.
At every index, I calculate the running sum and check if (prefix_sum - k) was seen before.
If yes, I use the distance between current and stored index to update the max length.
This allows me to find the longest subarray with sum = k in O(n) time and O(n) space,
and it handles both positive and negative numbers.”

"""
arr = [1, 2, 3]
k = 3

prefix_sum = 0
max_len = 0
seen = {}  # stores first occurrence of prefix_sum

for i in range(len(arr)):
    prefix_sum += arr[i]

    # Case 1: subarray from start has sum == k
    if prefix_sum == k:
        max_len = max(max_len, i + 1)

    # Case 2: subarray between two indices has sum == k
    if (prefix_sum - k) in seen:
        max_len = max(max_len, i - seen[prefix_sum - k])

    # store first occurrence only
    if prefix_sum not in seen:
        seen[prefix_sum] = i

print(max_len)



# Optimal Solution

"""
If all numbers ≥ 0,
you can use the sliding window (two-pointer) approach — O(1) space and O(n) time.

Steps:
	1.	Use two pointers: left and right.
	2.	Keep a running sum of the window.
	3.	Expand right while sum <= k.
	4.	If sum > k, shrink from left.
	5.	When sum == k, update max length.

Why not negatives:
    because the -ve can increase the sum while shrinking and vice versa
    Our approach works on the fact that adding elements increase the sum and vice versa.
"""
def longest_subarray_sum_k(arr, k):
    left = 0
    current_sum = 0
    max_len = 0

    for right in range(len(arr)):
        current_sum += arr[right]

        while current_sum > k and left <= right:
            current_sum -= arr[left]
            left += 1

        if current_sum == k:
            max_len = max(max_len, right - left + 1)

    return max_len
