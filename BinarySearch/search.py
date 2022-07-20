class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        #new idea: use lo and hi from article
        lo = 0
        hi = len(nums)-1
        mid = lo + int(len(nums)/2)
        
        while lo < hi:
            
            if target == nums[middle]:
                return middle
            
            elif target > nums[middle]:
                lo = mid
                
            else:#target < nums[middle]
                hi = mid - 1
        
        return -1

