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
        dupMap = set()  # value -> count

        for x in nums:
            if x not in dupMap:
                dupMap.add(x)
            else:
                return True
