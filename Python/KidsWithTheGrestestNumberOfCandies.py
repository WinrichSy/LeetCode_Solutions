#Kids With the Grestest Number of Candies
#https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        ans = [True if i+extraCandies>=max_candies else False for i in candies]
        return ans
