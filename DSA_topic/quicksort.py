def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort(left) + middle + quicksort(right)

# Example
arr = [3, 6, 8, 10, 1, 2, 1]
print(quicksort(arr))  # [1, 1, 2, 3, 6, 8, 10]

# How it works:

# 1.Pick a pivot (middle element)
# 2.Partition into three lists: elements less than, equal to, and greater than the pivot
# 3.Recursively sort left and right, then concatenate

# Time complexity: O(n log n) average, O(n²) worst case
# Space complexity: O(n)
# Want an in-place version or implementation in a different language?