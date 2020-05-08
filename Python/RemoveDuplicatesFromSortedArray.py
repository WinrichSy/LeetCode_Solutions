#Remove Duplicates From Sorted Array
#https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        i=1
        prev = nums[0]
        while(i<len(nums)):
          if prev == nums[i]:
            del nums[i]
          else:
            prev = nums[i]
            i+=1

        return len(nums)
