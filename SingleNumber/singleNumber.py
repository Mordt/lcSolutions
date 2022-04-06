class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return

        #new approach, find solo num
        currNum = nums[0]
        array = len(nums)

        for x in range(1, array):
            print(x)
            if nums[x] == currNum:
                continue
            else:
                return nums[x]
