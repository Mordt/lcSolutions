class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        #iterate backwards through string
        #count first non whitespace instance, return
        count = 0
        inWord = False
        for x in reversed(s):
            if x != ' ':
                inWord = True
                count += 1
            else:
                inWord = False

            if x == ' ' and count != 0:
                break

        return count
