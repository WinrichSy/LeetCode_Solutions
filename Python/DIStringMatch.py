#DI String Match
#https://leetcode.com/problems/di-string-match/

class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        i = 0
        j = len(S)
        ans = []
        for char in S:
            if char == 'I':
                ans.append(i)
                i += 1
            elif char == 'D':
                ans.append(j)
                j -= 1

        if S[-1] == 'I':
            ans.append(j)
        else:
            ans.append(i)
        print(ans)
        return ans
