class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        #use hashmap? trying to compare if every letter in string s exists in t
        #map every letter to every other letter?

        for i, x in enumerate(s):
            if x not in t[i]:
                return False

        #should be at the end of both strings
        return True
