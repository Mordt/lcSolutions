class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        #use bin() and int() to convert values then return
        bina = int(a, base = 2)
        binb = int(b, base = 2)
        
        result = bina + binb
        result = bin(result)
        
        result = result.replace('0b', '')
        return result        
