class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        #iterate backwards through string
        #count first non whitespace instance, return

        count = 0
        for x in reversed(s):
            if x != ' ':
                count += 1
            if x == ' ' and count != 0:
                break
        return count
