class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        #discussion:
        """
        obvious first solution is to brute force the thing, checking each element
        with every other element to find the solution, returning the indices as required
        this, however, takes O(n) time in the worst case. not good.
        
        what can we do instead? these are the data structures available to us:
            hashmaps is my first guess because of the complexity of everything
            perhaps sorting the nums list first might work.
            
        we will start with the brute force solution.
        
        toReturn = []
        for x in nums:
            for y in nums:
                #print(nums.index(y), nums.index(x))
                if nums.index(y) == nums.index(x):
                    
                    continue
                elif target-x == y:  
                    print("checck")
                    toReturn.insert(0, nums.index(x))
                    toReturn.insert(1, nums.index(y))
                    
                    return toReturn
        """
        #now the optimal solution

        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
