class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest = 0
        for x in nums:
            if largest + x >= largest:
                largest += x
            else:
                largest = 0

        return largest
