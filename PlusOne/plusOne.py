class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        #use not added flag to signify wheter current digit should be overflown
        #set to negative when addition has been complete
        #iterate through reversed digits for ease

        notAdded = True

        for i, x in enumerate(reversed(digits)):
            if notAdded:
                if x == 9:
                    x = 0
                    continue
                else:
                    x += 1
                    notAdded = False

        return digits
