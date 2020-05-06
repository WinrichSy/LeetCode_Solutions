#Container With Most Water
#https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_height = 0
        i = 0
        j = len(height)-1

        while(j>i):
            area = min(height[i], height[j])*abs(j-i)
            if max_height < area:
                max_height = area
            if (height[i] < height[j]):
                i += 1
            else:
                j -= 1

        return max_height
