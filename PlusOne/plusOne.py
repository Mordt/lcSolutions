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
        rev = reversed(digits)
        finalIndex = len(digits)

        for i, x in enumerate(rev):
            if notAdded:
                if i == finalIndex and x == 9:  # if most significant digit is 9
                    rev[i] = 0
                    rev.insert(len(rev), 1)
                    break
                if x == 9:
                    print(i, x)
                    rev[i] = 0
                    continue
                else:
                    rev[i] += 1
                    notAdded = False

        digits = reversed(rev)
        return digits
