#Happy Number
#https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        og_n = n
        if n==1:
            return True
        while(n > 3):
            n_list = str(n)
            n = 0
            for i in n_list:
                n += int(i)**2

            if n == 1:
                return True
            elif n == 4:
                return False
        return False
