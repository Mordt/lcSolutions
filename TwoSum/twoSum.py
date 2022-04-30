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
            for each number, we are looking for the difference between the target and the value
            for example if target = 4 and value = 1,
                we are looking for diff = 4-1 = 3
            can ignore the other numbers, jsut wanna know if 3 exists

            most efficient way is to make a hash map of every value in our input array
                so we can instantly check if the value 3 exists.
                
            in hashmap, map value of array to index.
            
        """