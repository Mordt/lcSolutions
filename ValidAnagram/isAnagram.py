class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        """
        Notes from vid explanation:
        
        using the characters of s, we can create the string t
        made up of exact same list of characters
        
        make hashmap of characters -> num of occurences?
        """
        if len(s) != len(t):
            return False

        smap = {}  # characters -> num of occurences
        tmap = {}

        for x, y in zip(s, t):
            if x not in smap:
                #add to map
                smap[x] = 1
            elif x in smap:
                smap[x] += 1

            if y not in tmap:
                tmap[y] = 1
            elif y in tmap:
                tmap[y] += 1

        # both maps should now be populated with values
        if smap == tmap:
            return True
        else:
            return False

        """
        Neetcode Solution:

        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True
        """

        """
        O(n) solution in terms of space
        sort the strings, add comparison
        cost is time complexity, nlogn time for a good sorting algorithm
        so sort both strings, compare. if equal, return true. else, return false.

        return sorted(s) == sorted(t)
        """