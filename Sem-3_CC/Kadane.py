from typing import List


def max_subarray(nums: List[int]) -> int:
    # cur  = jo subarray CURRENT index pe khatam ho raha hai uska best sum
    # best = ab tak ka sabse bada sum
    cur = best = nums[0]          # pehle element se shuru (all-negative array ke liye zaroori)

    for x in nums[1:]:
        cur = max(x, cur + x)     # extend karo ya naya start karo
        best = max(best, cur)

    return best


# Time: O(n), Space: O(1)


def dry_run(nums: List[int]) -> int:
    """Copy mein likhne wala dry run table print karta hai."""
    cur = best = nums[0]
    print(f"nums = {nums}")
    print(f"{'x':>3} | {'cur + x':>8} | {'cur = max(x, cur+x)':>20} | {'best':>5}")
    print("-" * 48)
    print(f"{nums[0]:>3} | {'-':>8} | {cur:>20} | {best:>5}   (start)")

    for x in nums[1:]:
        extend = cur + x
        cur = max(x, extend)
        best = max(best, cur)
        print(f"{x:>3} | {extend:>8} | {cur:>20} | {best:>5}")

    print(f"\nAnswer = {best}\n")
    return best


if __name__ == "__main__":
    dry_run([-2, 1, -3, 4, -1, 2, 1, -5, 4])   # 6  (subarray [4, -1, 2, 1])
    dry_run([-3, -1, -2])                      # -1 (all negative)
    print(max_subarray([5, 4, -1, 7, 8]))      # 23