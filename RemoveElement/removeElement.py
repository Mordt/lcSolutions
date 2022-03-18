class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:
            nums.remove(val)
                
        return len(nums)

    #alternate solution:
    """
    count=0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[count] = nums[i]
            count +=1
    return count

    """
