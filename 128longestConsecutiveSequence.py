class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        num_set = set(nums)
        res = 0 

        for num in num_set:
            if num -1 not in num_set:
                current_num = num
                current_res = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_res += 1
                res = max(res, current_res)

        return res
# Time complexity: O(n)