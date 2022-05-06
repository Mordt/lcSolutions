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

        buy = 0, sell = 1
        maxProfit = 0

        while buy < len(prices):
            #isprofitable?
            if buy < sell:
                profit = sell - buy
                if profit > maxProfit:
                    maxProfit = profit
                sell += 1
            else:
                buy += 1
                sell += 1
