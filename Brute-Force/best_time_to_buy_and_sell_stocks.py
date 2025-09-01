from typing import List


class Solution:
    """
    Problem Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
    - 121. Best Time to Buy and Sell Stock
    
    Learnings:
    - O(n^2) is not good for large inputs, we should always further reduct it to O(n) for better and faster results.
    """
    def maxProfit(self, prices: List[int]) -> int:
        # Brute Force Solution: fails when input is too big!

        # Set max_profit at 0, a case when no profit is found!
        # Start i from 0 to prices list length
        # Start inner for-loop from ith-index to length of the array
        # if price at ith day is smaller then find the profit and check 
        # whether the profit value is greater than the value stored in max_profit.
        # increment the ith day by 1.

        arr_length = len(prices)
        max_profit = 0
        i = 0
        while i < arr_length:
            for j in range(i+1, arr_length):
                if prices[i] < prices[j]:
                    profit = prices[j] - prices[i]
                    max_profit = max(max_profit, profit)
            i+=1

        return max_profit

