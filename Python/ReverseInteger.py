#Reverse Integer
#https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:

        #Handle Negatives First
        negative = False
        if x<0:
            negative = True
            x = str(x)[1:]

        #get length of string
        length = len(str(x))

        #put string in reverse order
        string_x = str(x)[::-1]
        total = 0

        for i in range(length):
            total += int(string_x[i])*(10**(length-1))
            length -= 1

        if total>(2**31)-1 or -total<-(2**31):
            return 0

        if negative:
            return -total

        return total
