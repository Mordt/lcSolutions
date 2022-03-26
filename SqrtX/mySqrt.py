class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        #what number, between 1 and x times itself is equal to x?
        #cant do this:
            #return int(sqrt(x))
        #idea instead search small integer space of possible answers and see
        #if num*num = x
        integers = range(1,x)
        domain = []
        for num in integers:
            if num*num > x:
                domain = range(1,num)
                break
        return domain[len(domain)-1]

