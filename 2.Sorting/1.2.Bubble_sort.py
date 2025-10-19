"""
Problem statement: to sort the list in the descending order ?

So in bubble sorting, what what we have to do?
So start with the first index and check the index next to it, whether its value is greater or not
If it is greater we do the swapping
"""
arr = [3,7,2,8,9,1,6]
n = len(arr)


for i in range(0,n-1): # first dry run the code you will get to know why (Because if we reach index n-1 aour swapping is done)
    for j in range(0,n-1-i): # last index is sorted so removing from the loop
        if arr[j+1] > arr[j]:
            arr[j], arr[j+1] = arr[j+1], arr[j] # two pointer swapping
print(arr)


