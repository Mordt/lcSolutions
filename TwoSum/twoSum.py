class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #Day 2
        #discussion:
        """
        obvious first solution is to brute force the thing, checking each element
        with every other element to find the solution, returning the indices as required
        this, however, takes O(n) time in the worst case. not good.
        
        what can we do instead? these are the data structures available to us:
            hashmaps is my first guess because of the complexity of everything
            perhaps sorting the nums list first might work.
            
        we will start with the brute force solution.
        """
        toReturn = []
        for x in nums:
            for y in nums:
                if y == x:
                    continue
                if target-x == y:
                    toReturn.insert(0, nums.index(x))
                    toReturn.insert(1, nums.index(y))
                    
                    return toReturn
