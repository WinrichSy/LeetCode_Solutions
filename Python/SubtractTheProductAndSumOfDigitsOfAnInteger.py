#Subtract the Product and Sum of Digits of an Integer
#https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

import math
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = [int(i) for i in str(n)]
        return math.prod(digits)-sum(digits)
