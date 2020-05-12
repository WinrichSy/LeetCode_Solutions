#Split a String in Balanced Strings
#https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        if len(s)==1:
            return 1
        ans = 0
        L = 0
        R = 0
        for i in s:
            if i == 'L':
                L += 1
            elif i == 'R':
                R += 1
            if L==R:
                ans += 1
                L = 0
                R = 0

        return ans
