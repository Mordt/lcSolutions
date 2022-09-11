class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #without division, will need to multiply product of values before with
        #product of values after
        #will need to create prefix array
        #create postfix array from prefix array
        
        prefix = [1] * (len(nums))
        postfix = [1] * (len(nums))
        
        i = 0
        pre = 1
        for n in nums:
            pre = pre * n
            prefix[i] = pre
            i += 1
        
        i = len(postfix)
        i -= 1
        post = 1
        for n in reversed(nums):
            post = post * n
            postfix[i] = post
            i -= 1
            
        print(prefix)
        print(postfix)

#my earlier solution:


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
