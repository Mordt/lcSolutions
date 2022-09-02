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
        
        if not stones:
            return 0
        else:
            return stones[0]

#neetcode solution below:

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)

        stones.append(0)
        return abs(stones[0]) 
