#Backspace String Compare
#https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i = 0
        while(i<len(S)):
            if S[i] == '#' and i==0:
                S = S[1:]
            elif S[i] == '#':
                S = S[:i-1] + S[i+1:]
                i -= 1
            else:
                i+=1

        j = 0
        while(j<len(T)):
            if T[j] == '#' and j==0:
                T = T[1:]
            elif T[j] == '#':
                T = T[:j-1] + T[j+1:]
                j -= 1
            else:
                j+=1

        return S==T
