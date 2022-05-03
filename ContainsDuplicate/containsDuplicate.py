class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """
        data = set()
        for i in nums:
            if i in data:
                return True
            data.add(i)
        return False
        """
        #new solution
        dupMap = {}  # value -> count

        for x in nums:
            if x not in dupMap:
                dupMap[x] = 1
            else:
                return True
