class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        #heap/priority queue
        #sort the list, smash from heaviest to lightest
        
        
        while len(stones) > 1:
            stones.sort()
            y = stones.pop()
            x = stones.pop()
            
            if x == y:
                continue
            else:
                y -= x
                stones.insert(0, y)
        
        return stones[0]
    
