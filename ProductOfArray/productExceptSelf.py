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
        
        pre = [1] * (len(nums))
        post = [1] * (len(nums))
        
        i = 0
        for n in nums:
            #pre[i] = pre[i] * n
            print(i)
            i += 1
            
        #print(pre)


