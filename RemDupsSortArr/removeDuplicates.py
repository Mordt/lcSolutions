class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for i, x in enumerate(nums):
            print(nums)
            if i+1 < len(nums):
                while x == nums[i+1]:  # if equal to next
                    nums.pop(i)

        k = len(nums)
        return k