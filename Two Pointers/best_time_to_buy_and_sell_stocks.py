from typing import List


class Solution:
    """
    Problem Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
    - 121. Best Time to Buy and Sell Stock
    Time complexity: O(n)
    Space complexity: O(1)

    Learnings:
    - Used O(n) time complexity for better results
    - Used two pointers to keep track of min price to buy and max profit from it.
    """
    def maxProfit(self, prices: List[int]) -> int:
        # O(n) (TWO POINTERS) approach ->
        # define two variables -> 
        #   - max_profit => profit gained
        #   - min_price_to_buy => best time to buy at lowest price

        # loop through the prices array and check
        # whether on a day the price is lower than others, 
        # profit happened by subtracting the today's price from min_price of the stocks
        # comparing the max profit
        max_profit = 0
        min_price_to_buy = float("inf")
        
        for today in range(len(prices)):
            if min_price_to_buy > prices[today]:
                min_price_to_buy = prices[today]
            profit = prices[today] - min_price_to_buy
            if profit > max_profit:
                max_profit = profit
        return max_profit

