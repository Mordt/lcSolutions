class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        elif x == 1:
            return 1
        root = x / 2
        eps = 0.00001
        while(root - x / root > eps):
            root = 0.5 * (root + x / root)
        return int(root)

