class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return

        #new approach, find solo num
        #check left and right
        currNum = nums[0]
        array = len(nums)

        for x in range(1, array):
            if nums[x] == currNum:
                continue
            else:
                currNum = nums[x]
                return nums[x]
