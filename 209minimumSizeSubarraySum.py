class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        sum_cur = 0
        min_length = float('inf')

        for right in range(len(nums)):
            sum_cur += nums[right]

            while sum_cur >= target:
                min_length = min(min_length, right - left + 1)
                sum_cur -= nums[left]
                left += 1

        return 0 if min_length == float('inf') else min_length 