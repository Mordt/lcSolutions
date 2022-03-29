class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #dynamic programming really
        #emulates fibonacci sequence
        #count from top to bottom to find solution

        one, two = 1,1

        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one