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
        #otherwise, map a new value into the hashmap
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

        """
        notes from video solution:
        type of problem: arrays and hashing
            first instinct is obviously to brute force with a nested loop, O(n^2)

        """