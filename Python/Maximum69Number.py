#Maximum 69 Number
#https://leetcode.com/problems/maximum-69-number/

class Solution:
    def maximum69Number (self, num: int) -> int:
        str_num = str(num)
        if str_num.count('6')==0:
            return num

        str_num = list(str_num)
        str_num[str_num.index('6')]='9'
        return int(''.join(str_num))
