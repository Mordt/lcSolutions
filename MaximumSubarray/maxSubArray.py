class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = nums[0]
        curSum = 0
        for n in nums:
            curSum += n  # add current sum to each value
            maxSum = max(curSum, maxSum)
            curSum = max(0, curSum)
        return maxSum
