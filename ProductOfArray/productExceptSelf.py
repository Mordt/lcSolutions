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
        result = [1] * (len(nums))

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

        # have created both prefix and postfix,
        #now create result which is product of all prev
        # * product of all post

        pre = 1
        post = 1
        i = 0
        for n in nums:
            j = i + 1
            if j < len(nums):
                result[i] = pre * postfix[j]
                pre = prefix[i]
            else:  # final element
                j = i - 1
                result[i] = post * prefix[j]

            i += 1

        return result

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
