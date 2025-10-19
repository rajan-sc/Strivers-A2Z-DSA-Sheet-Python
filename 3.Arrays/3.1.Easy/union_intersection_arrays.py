"""
Problem Statement:
Union intersection of two arrays
"""


a = [1,2,3,4,5]
b = [3,4,6,7,7]


# brute force

s = set()

for i in a:
    if i not in s:
        s.add(i)
for i in b:
    if i not in s:
        s.add(i)

print(s)


# t.c = O(n+m)
a = [1,2,3,4,5]
b = [3,4,6,7,7]

"""
Optimized approach
"""

def union(a, b):
    union = []
    n1 = len(a)
    n2 = len(b)
    i = 0
    j = 0

    while i < n1 and j < n2:
        if a[i] <= b[j]:
            if len(union) == 0 or union[-1] != a[i]:
                union.append(a[i])
            i += 1
        else:
            if len(union) == 0 or union[-1] != b[j]:
                union.append(b[j])
            j += 1

    while i < n1:
        if len(union) == 0 or union[-1] != a[i]:
            union.append(a[i])
        i += 1

    while j < n2:
        if len(union) == 0 or union[-1] != b[j]:
            union.append(b[j])
        j += 1

    return union

print(union(a, b))


# t.c = O(n1+n2) and space = O(n1+n2)


"""
Intersection of two arrays:
"""

a = [1,2,3,3,3,4,5]
b = [3,3,4,6,7,7]

"""
brute approach

Make a new visitor array of the same length as b
And check if i is equal to j and the visitor position value is zero
If you find the matching element, add that to the ans and update the visitor j position to 1
"""

def intersection(a, b):
    ans = []
    n1 = len(a)
    n2 = len(b)
    visitor = [0] * len(b)

    for i in range(0, n1):
        for j in range(0, n2):
            if a[i] == b[j] and visitor[j] == 0:
                ans.append(a[i])
                visitor[j] = 1
                break
            if b[j] > a[i]:
                break
    return ans


print(intersection(a, b))

# t.c = O(n^2) s.c = O(n)

"""
Optimized approach two pointers
"""

def o_intersection(a, b):
    ans = []
    n1 = len(a)
    n2 = len(b)

    i = j = 0

    while i < n1 and j < n2:
        if a[i] == b[j]:
            ans.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else :
            j += 1
    return ans

print(o_intersection(a, b))
