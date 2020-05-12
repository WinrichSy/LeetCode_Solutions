#Find Numbers with Even Number of Digits
#https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            if len(str(i))%2==0:
                ans += 1

        return ans
