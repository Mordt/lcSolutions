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
        
        if x == 0:
            return 0
        if x == 1:
            return 1
        
        integers = range(0,x)
        domain = []
        for num in integers:
            if num*num > x:
                domain = range(0,num)
                break
            if num*num == x:
                domain = range(0, num)
                break
            domain = range(0,num)
        print(integers)
        return domain[len(domain)-1

        
