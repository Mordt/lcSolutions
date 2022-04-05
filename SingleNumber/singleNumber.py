class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return

        currNum = nums[0]
        array = len(nums)

        for x in range(1, array-1):
            print(x, array, nums)
            if nums[x] == currNum:
                nums.remove(nums[x])
                continue
            else:
                currNum = nums[x]
                continue

            #print(currNum, nums[x])
