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

        for x in s:
            if x.isalnum():
                print(x.lower())
