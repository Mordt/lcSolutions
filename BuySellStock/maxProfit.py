class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """
        Brainstorming:
        lowest value must be before highest value
        one solution would be to scan, find the lowest value and highest
        if highest val is before lowest, discard and search for next highest
        return that difference
        """
        #new approach, have two pointers adjacent to each other, if left < right, increment right only
        #otherwise increment both
        #when best is reched, return difference

        #neetcode:
        #calculate profit every time, wanna keep it positive
        #if right is less than left, update pointers to the right
        #if right val is greater than left, record profit, record max if bigger than curr max
        #leave left ptr, only update right pointer
        #keep iterating till the max is bigger
        #once at end, return max profit value
        #mem is O(1), time is O(n)

        #this is our sliding window though, it's our two pointers adjacent to each other checking for certain conditions
        #ain't so bad all things considered.

        buy = 0
        sell = 1
        maxProfit = 0

        while sell < len(prices):
            #isprofitable?
            if prices[buy] < prices[sell]:#ensuring the price we're looking at makes sense
                profit = prices[sell] - prices[buy]
                if profit > maxProfit:#obviously take max profit
                    maxProfit = profit
            else:#otherwise, our buy is pointing to something higher than our sell, which doesn't work
                buy = sell#increment.
            sell += 1

        return maxProfit
