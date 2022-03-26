class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        #what number, between 1 and x times itself is equal to x?
        #cant do this:
            #return int(sqrt(x))
        integers = range(1,x)
        for num in integers:
            if num*num == x:
                return num       
