# Best Time to Buy and Sell Stock
# Solved 
# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

# You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

# Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

# Example 1:

# Input: prices = [10,1,5,6,7,1]

# Output: 6
# Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

# Example 2:

# Input: prices = [10,8,7,5,2]

# Output: 0
# Explanation: No profitable transactions can be made, thus the max profit is 0.

# Constraints:

# 1 <= prices.length <= 100
# 0 <= prices[i] <= 100


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)

        return max_profit

# BruteForce Solution:
# This solution uses two nested loops to check all pairs of days.
# It calculates the profit for each pair and keeps track of the maximum profit found.
# Time Complexity: O(n^2)
# Space Complexity: O(1)


def maxProfit(prices):
    l, r = 0,1
    maxprofit = 0

    while (r<len(prices)):
        if prices[r] > prices[l]:
            profit = prices[r] - prices[l]
            maxprofit = max(maxprofit, profit)
        
        else:
            l = r
        
        r+=1
    
    return maxprofit

# Two Pointer Solution:
# This solution uses two pointers, one at the start and one at the next day.
# It checks if the price on the right pointer is greater than the price on the left pointer.
# If it is, it calculates the profit and updates the maximum profit if necessary.
# If the price on the right pointer is less than or equal to the price on the left pointer, it moves the left pointer to the right.
# This way, it ensures that it always considers the maximum possible profit while iterating through the prices.
# Time Complexity: O(n)

# Space Complexity: O(1)
print("Maxx profit is:  ", maxProfit([10,1,5,6,7,1]))