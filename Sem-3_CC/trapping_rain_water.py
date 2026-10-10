from typing import List


def trap(height: List[int]) -> int:
    # l, r = dono ends pe pointers
    l, r = 0, len(height) - 1
    left_max = right_max = water = 0

    while l < r:
        if height[l] < height[r]:          # LEFT side chhoti hai
            if height[l] >= left_max:
                left_max = height[l]       # nayi unchi bar, paani nahi
            else:
                water += left_max - height[l]   # gaddha, paani bharo
            l += 1
        else:                              # RIGHT side (mirror)
            if height[r] >= right_max:
                right_max = height[r]
            else:
                water += right_max - height[r]
            r -= 1

    return water


# Time: O(n), Space: O(1)

if __name__ == "__main__":
    print(trap([3, 0, 2, 0, 4]))                       # 7
    print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
    print(trap([4, 2, 0, 3, 2, 5]))                    # 9