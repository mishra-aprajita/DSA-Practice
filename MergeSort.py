def merge_sort(arr):
    # If array has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Find the middle point
    mid = len(arr) // 2
    
    # Split array into two halves
    left = arr[:mid]
    right = arr[mid:]
    
    # Recursively sort both halves
    left = merge_sort(left)
    right = merge_sort(right)
    
    # Merge the sorted halves
    return merge(left, right)


def merge(left, right):
    result = []
    i = 0  # pointer for left array
    j = 0  # pointer for right array
    
    # Compare elements from left and right, add smaller one first
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements from left (if any)
    while i < len(left):
        result.append(left[i])
        i += 1
    
    # Add remaining elements from right (if any)
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result


# Test the code
arr = [38, 27, 43, 3, 9, 82, 10]
print("Original:", arr)
sorted_arr = merge_sort(arr)
print("Sorted:", sorted_arr)