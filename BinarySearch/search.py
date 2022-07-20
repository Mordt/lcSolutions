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
            mid = lo + (hi-lo)/2
            if target == nums[mid]:
                return mid
            
            elif target > nums[mid]:
                lo = mid + 1
                
            else:#target < nums[mid]
                hi = mid - 1
        
        return -1

