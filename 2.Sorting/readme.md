
# Sorting Algorithms Comparison

## 🔹 1. Selection Sort

### Idea
Find the smallest (or largest) element and place it at the correct position in each pass.

### How it works
```
arr = [3, 1, 4, 2]

Pass 1 → find min(3,1,4,2) = 1 → swap with arr[0]
arr = [1, 3, 4, 2]

Pass 2 → find min(3,4,2) = 2 → swap with arr[1]
arr = [1, 2, 4, 3]

Pass 3 → find min(4,3) = 3 → swap with arr[2]
arr = [1, 2, 3, 4]
```

✅ **Key points:**
- Always finds minimum and places it in the front.
- Swaps fewer times (at most n-1 swaps).
- Does not stop early even if array is sorted.

⏱ **Time Complexity:**
- Best = Average = Worst = `O(n²)`
- Space: `O(1)`


## 🔹 2. Bubble Sort

### Idea
Repeatedly swap adjacent elements if they are in the wrong order.
After every pass, the largest element “bubbles” to the end.

### Example
```
arr = [3, 1, 4, 2]

Pass 1 → compare and swap:
(3,1) → [1,3,4,2]
(3,4) → [1,3,4,2]
(4,2) → [1,3,2,4]

Pass 2 → [1,2,3,4]
```

✅ **Key points:**
- Can stop early if array becomes sorted (use a flag).
- Simple, good for small datasets.

⏱ **Time Complexity:**
- Best = `O(n)` (already sorted)
- Average = Worst = `O(n²)`
- Space: `O(1)`


## 🔹 3. Insertion Sort

### Idea
Build the sorted array one element at a time — like sorting playing cards in your hand.

### Example
```
arr = [3, 1, 4, 2]

Take 1 → insert into sorted [3] → [1,3,4,2]
Take 4 → insert correctly → [1,3,4,2]
Take 2 → insert correctly → [1,2,3,4]
```

✅ **Key points:**
- Good for small or nearly sorted arrays.
- Stable sort (keeps order of equal elements).
- Used in hybrid algorithms like **Timsort** (Python’s `.sort()`).

⏱ **Time Complexity:**
- Best = `O(n)`
- Average = Worst = `O(n²)`
- Space: `O(1)`


## ⚔️ Comparison Table

| Feature | Selection Sort | Bubble Sort | Insertion Sort |
|----------|----------------|--------------|----------------|
| **Basic Idea** | Pick min & place | Swap adjacent if wrong | Insert element into sorted part |
| **Best Case** | O(n²) | O(n) | O(n) |
| **Average Case** | O(n²) | O(n²) | O(n²) |
| **Worst Case** | O(n²) | O(n²) | O(n²) |
| **Stable** | ❌ No | ✅ Yes | ✅ Yes |
| **In-place** | ✅ Yes | ✅ Yes | ✅ Yes |
| **Swaps** | Few | Many | Medium |
| **Stops Early?** | ❌ No | ✅ Yes | ✅ Yes |
| **Good For** | Small arrays | Teaching / small data | Nearly sorted data |

---

## 🧠 Interview Tips

- **If array is almost sorted:** ✅ Use *Insertion Sort* (runs nearly O(n)).
- **If you want fewer swaps:** ✅ Use *Selection Sort*.
- **If you want early detection of sorted array:** ✅ Use *Bubble Sort*.
