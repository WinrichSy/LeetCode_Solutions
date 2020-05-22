#Hamming Distance
#https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        if x == y:
            return 0
        x_bin = bin(x).replace('b','')
        y_bin = bin(y).replace('b','')
        xlen = len(x_bin)
        ylen = len(y_bin)
        if xlen < ylen:
            for i in range(ylen-xlen):
                x_bin = '0'+x_bin
        elif ylen < xlen:
            for i in range(xlen-ylen):
                y_bin = '0'+y_bin

        x_ones = set([idx for idx, val in enumerate(x_bin) if val=='1'])
        y_ones = set([idx for idx, val in enumerate(y_bin) if val=='1'])
        differences = x_ones^y_ones

        return(len(differences))
