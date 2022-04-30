class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #assuming step one is  creating the hashmap
        prevMap = {}  # val -> index

        #iterate through nums array, record difference
        #if in hashmap, return indexes
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
