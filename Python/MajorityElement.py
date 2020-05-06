#Majority Element
#https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        unique_nums = []
        for i in nums:
            if i not in unique_nums:
                unique_nums.append(i)

        answer = 0
        for j in unique_nums:
            if nums.count(answer) < nums.count(j):
                answer = j

        return answer
