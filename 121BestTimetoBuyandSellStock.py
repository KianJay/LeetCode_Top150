"""You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize the maximum profit to 0
        max_profit = 0
        # Initialize the minimum price to infinity
        min_price = float('inf')
      
        # Loop through the prices
        for price in prices:
            # Update the maximum profit if the current price minus the minimum price seen so far is greater
            max_profit = max(max_profit, price - min_price)
            # Update the minimum price seen so far if the current price is lower
            min_price = min(min_price, price)
          
        # Return the maximum profit achieved
        return max_profit