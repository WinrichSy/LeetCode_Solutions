#Partition Equal Subset Sum
#https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        num_sum = sum(nums)
        if num_sum%2!=0:
            return False

        #if sums is even, then find the sum portions that equals that
        needed_sum = num_sum//2
        i, j = 0,0

        part = [[ True for i in range(len(nums) + 1)]
                   for j in range(needed_sum + 1)]

        # initialize top row as true
        for i in range(0, len(nums) + 1):
            part[0][i] = True

        # initialize leftmost column,
        # except part[0][0], as 0
        for i in range(1, needed_sum + 1):
            part[i][0] = False

        # fill the partition table in
        # bottom up manner
        for i in range(1, needed_sum + 1):

            for j in range(1, len(nums) + 1):
                part[i][j] = part[i][j - 1]

                if i >= nums[j - 1]:
                    part[i][j] = (part[i][j] or
                                  part[i - nums[j - 1]][j - 1])

        return part[needed_sum][len(nums)]
