class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #two pointers type question
        # one pointer at each end, iterate thru and compare if equal
        # step one is to get rid of capitals and remove non alphanumerics
        # step two is to take that string and compare it to its reversal and see if theyre equal
        # if so, is palindrome. return true

        #new string solution:
        #problem is that there is an isalnum() library function, plus wasted memory
        #with the creation of two new strings (newStr and reversed newStr)
        """newStr = ""
        
        for x in s:
            if x.isalnum():
                newStr += x.lower()
                
        #syntax to reverse a string python: string[::-1]
        return newStr == newStr[::-1]"""

        #two pointer attempt:
        leftPtr = s[0]
        rightPtr = s[len(s)-1]
        for i, x in enumerate(s):
            if

        """
        helper function to check if a value is alphanumeric
        def alphaNum(self,c ):
            return (ord('A') <= ord(c) <= ord('Z') or
                    ord('a') <= ord(c) <= ord('z') or
                    ord('0') <= ord(c) <= ord('9'))
            
        """
