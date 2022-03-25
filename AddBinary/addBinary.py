class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        #use bin() and int() to convert values then return
        deca = int(a)
        decb = int(b)
        result = deca + decb
        
        return = bin(result)       
