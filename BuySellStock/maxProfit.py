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
        
        bindex = 0
        sindex = 0
        
        for i, x in enumerate(prices):
            if x < buy:
                buy = x
                bindex = i
            if x > sell:
                sell = x
                sindex = i
                
        #new approach, have two pointers adjacent to each other, if left < right, increment right only
        #otherwise increment both
        #when best is reched, return difference
                

            
        