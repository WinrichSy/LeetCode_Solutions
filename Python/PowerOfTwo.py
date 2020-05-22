#Power of Two
#https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False

        return bin(n).count('1') == 1
