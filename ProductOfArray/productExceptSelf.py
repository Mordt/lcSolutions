class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #idea: go through nums,
        #create map of self -> product without self

        product = 1
        for n in nums:
            product = product * n

        prodSans = {}
        for n in nums:
            prodSans[n] = product/n

        result = []
        for key in prodSans:
            result.append(prodSans[key])

        return result
