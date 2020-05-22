#Cells With Odd Values in a Matrix
#https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

from numpy import zeros, ones

class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        matrix = zeros((n,m))
        one = ones((n,m))

        for i in indices:
            row = i[0]
            column = i[1]
            matrix[row,:] += one[row,:]
            matrix[:,column] += one[:,column]

        ans = 0
        for i in matrix:
            for j in i:
                if j%2!=0:
                    ans+=1

        return ans
