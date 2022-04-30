class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s.length() != t.length():
            return false
        #use hashmap? trying to compare if every letter in string s exists in t

        for i, x in enumerate s:
