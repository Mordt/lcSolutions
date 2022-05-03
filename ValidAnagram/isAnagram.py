class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False
        #the below works in every case where there are no repeated letters
        """
        for x in s:
            if x not in t:
                return False
            
        #should be at the end of both strings
        return True
        """

        """
        Notes from vid explanation:
        
        using the characters of s, we can create the string t
        made up of exact same list of characters
        
        make hashmap of characters -> num of occurences?
        """
        #attempt:
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
            elif y in smap:
                tmap[y] += 1

        # both maps should now be populated with values
        if smap == tmap:
            return True
        else:
            return False
