#Best Time to Buy and Sell Stock II
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        running_total = 0
        for idx, val in enumerate(prices[:-1]):
            if val < prices[idx+1]:
                running_total += (prices[idx+1]-val)

        return running_total
