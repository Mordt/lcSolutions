class Solution(object):
    def isAnagram(s, t):
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

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #strategy is to compare whether anagrams are valid, if so, group
        #by calling is anagram
        for x in strs:
            for y in strs:
                #for x, i in enumerate(strs):
                #    print(x, i)
