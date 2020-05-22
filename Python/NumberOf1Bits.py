#Number of 1 Bits
#https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        return len([1 for i in bin(n) if i=='1'])
