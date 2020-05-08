#Single Number
#https://leetcode.com/problems/single-number/

import collections

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        for key, val in counts.items():
            if val == 1:
                return key
