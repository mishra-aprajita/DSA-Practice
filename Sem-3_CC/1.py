def lower_bound(arr, x):
    lo, hi = 0, len(arr)

    while lo < hi:
        mid = lo + (hi - lo) // 2

        if arr[mid] >= x:
            hi = mid
        else:
            lo = mid + 1

    return lo


def upper_bound(arr, x):
    lo, hi = 0, len(arr)

    while lo < hi:
        mid = lo + (hi - lo) // 2

        if arr[mid] > x:
            hi = mid
        else:
            lo = mid + 1

    return lo


# Test the functions
arr = [1, 2, 2, 2, 4, 5, 7]
x = 2

print("Lower Bound Index:", lower_bound(arr, x))
print("Upper Bound Index:", upper_bound(arr, x))
print("Number of occurrences:", upper_bound(arr, x) - lower_bound(arr, x))