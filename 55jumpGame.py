"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
"""
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        goal_post = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal_post:
                goal_post = i

        return (goal_post == 0)
'''
We're going to initialize a goal post, which is initially the last index.
We're going to setup a For Loop that iterates over the array backwards.
We ask each element 'Can you jump to or over the goal post from here?' if so, we set the goal post to that element.
If not, we continue looping.
We repeat this logic until we've been through the entire array.
Is the goal post now at the first index? If so we can jump to the last index, if not, we cannot jump to it.
'''