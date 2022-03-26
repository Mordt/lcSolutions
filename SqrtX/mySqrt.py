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
        domain = []
        for num in integers:
            if num*num >= x:
                print num
                domain = range(1,num)
                break
        print(domain)
        return domain[len(domain)-1]
