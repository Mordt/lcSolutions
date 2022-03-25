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
        bin(result)
        result = str(result)
        
        return result.decode('ascii')       
