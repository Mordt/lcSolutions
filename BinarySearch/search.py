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
                highMid = int((len(nums)-middle)/2)
                middle += highMid
                continue
                
            else:#target < nums[middle]
                middle = int(middle/2)
                continue
        
        return -1

