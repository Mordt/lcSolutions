class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return false
        #use hashmap? trying to compare if every letter in string s exists in t

        for x in enumerate(s):
            print(x)
