from typing import List


def sort_colors(nums: List[int]) -> None:
    # 3 pointers:
    # [0 .. low-1]   -> sab 0
    # [low .. mid-1] -> sab 1
    # [mid .. high]  -> unknown (abhi check karna hai)
    # [high+1 .. n]  -> sab 2
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1                 # swap mein 1 aaya (ya same 0), safe hai
        elif nums[mid] == 1:
            mid += 1                 # 1 sahi jagah pe hai
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1                # mid aage NAHI badhana (naya value check nahi hua)


# Time: O(n), Space: O(1)

if __name__ == "__main__":
    a = [2, 0, 2, 1, 1, 0]
    sort_colors(a)
    print(a)   # [0, 0, 1, 1, 2, 2]

    b = [2, 0, 1]
    sort_colors(b)
    print(b)   # [0, 1, 2]

    c = [1, 2, 0, 1, 0, 2, 2]
    sort_colors(c)
    print(c)   # [0, 0, 1, 1, 2, 2, 2]