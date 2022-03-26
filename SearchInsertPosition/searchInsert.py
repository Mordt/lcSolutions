class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        #first idea was to insert in order,
        #however this required an additional library, and I didn't
        #want to do that.
        #instead, i thought it would be smarter to insert, sort, then
        #return the index :)
        
        if target in nums:
            return nums.index(target)
        else:
            nums.insert(0, target)
            nums.sort()
            return nums.index(target)
           
