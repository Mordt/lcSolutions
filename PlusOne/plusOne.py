class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        #new idea
        #convert to a number, add it then convert back to a list
        #comments for testing, hello father
        num = 0
        for i in range(len(digits)):
            num += digits[i] * pow(10, (len(digits)-1-i))
            
        num += 1
        return [int(i) for i in str(num)]
