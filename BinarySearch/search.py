class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        middle = int(len(nums)/2)
        
        while True:
            
            if target == nums[middle]:
                return middle
            
            elif target > nums[middle]:
                highMid = len(nums)-middle
                middle = int(highMid/2)
                continue
            else:#target < nums[middle]
                middle = int(middle/2)
                continue
        
        return -1


