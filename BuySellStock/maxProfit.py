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

        for i, x in enumerate(prices):
            print(i, x)
