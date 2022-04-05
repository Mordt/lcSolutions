class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return

        crrNum = nums[0]

        array = len(nums)
        for x in array:
            print(nums[x])
