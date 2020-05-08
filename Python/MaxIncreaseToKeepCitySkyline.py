#Max Increase to Keep City Skyline
#https://leetcode.com/problems/max-increase-to-keep-city-skyline/

import numpy as np
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:

        numpy_grid = np.array(grid)
        left_right = [max(i) for i in numpy_grid]
        top_bottom = [max(numpy_grid[:,i]) for i in range(len(numpy_grid))]

        new_grid_sum = 0
        for i in left_right:
            for j in top_bottom:
                new_grid_sum += min([i,j])

        return new_grid_sum-(sum(sum(numpy_grid)))
