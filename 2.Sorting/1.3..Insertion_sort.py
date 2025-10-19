"""
Same as deck of cards in your hand you place 1 card first which is already sorted and then add the cards before or after it.

key = arr[i] → pick the current element.

Compare it with the sorted portion (arr[0..i-1]).

While elements are smaller than key (because descending order), shift them right.

Insert key at the correct position (j + 1).
"""
arr = [23, 45, 56, 23, 96, 12]
n = len(arr)

for i in range(1, n):
    key = arr[i]   # current element to insert
    j = i - 1

    # shift elements that are smaller than key to the right
    while j >= 0 and arr[j] < key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key   # place key at correct position

print(arr)


# Sample array
arr = [23, 45, 56, 23, 96, 12]
n = len(arr)  # Length of the array

# Outer loop: start from the second element (index 1) to the end
for i in range(1, n):
    j = i  # Initialize j as the current index

    # Inner loop: move the current element backward in the sorted portion
    # Condition: j > 0 (not beyond the first element)
    #            arr[j] > arr[j-1] (for descending order)
    while j > 0 and arr[j] > arr[j-1]:
        # Swap arr[j] and arr[j-1] to move the larger element left
        arr[j], arr[j-1] = arr[j-1], arr[j]
        j -= 1  # Move one step backward

# Print the final sorted array in descending order
print(arr)
