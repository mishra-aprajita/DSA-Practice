class Solution:
    def maxProduct(self, nums):
        curr_max = nums[0]
        curr_min = nums[0]
        answer = nums[0]

        for i in range(1, len(nums)):
            n = nums[i]

            if n < 0:
                curr_max, curr_min = curr_min, curr_max

            curr_max = max(n, curr_max * n)
            curr_min = min(n, curr_min * n)

            answer = max(answer, curr_max)
        return answer
    
