class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor = nums[0]
        for i in range(1, len(nums)):
            xor ^= nums[i]
        return xor
