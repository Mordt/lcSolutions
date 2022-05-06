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
        buy = 0
        sell = 0

        b = 0
        s = 1

        for i, x in enumerate(prices):
            if prices[b] < prices[s]:  # buy is 7 and sell is 1, for example
                b += 1
                s += 1
                buy = prices[b]
                sell = prices[s]
            else:
                if x < buy:
                    buy = x

                if x > sell:
                    sell = x
                s += 1
                b += 1
        #new approach, have two pointers adjacent to each other, if left < right, increment right only
        #otherwise increment both
        #when best is reched, return difference
