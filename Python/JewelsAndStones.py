#Jewels and Stones
#https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        ans = 0
        for i in J:
            ans += S.count(i)

        return ans
