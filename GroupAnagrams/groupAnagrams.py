class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #new idea:
        #hashmap mapping letters to words
        #so count e, count a, count t, mapped to the words that have them

        result = {}  # char count of each string -> list of anagrams

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")]
