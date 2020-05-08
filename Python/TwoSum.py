#Two Sum
#https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for iidx, ival in enumerate(nums[:-1]):
            for jidx, jval in enumerate(nums[iidx+1:]):
                if ival+jval == target:
                    return[iidx, jidx+iidx+1]

        return []
