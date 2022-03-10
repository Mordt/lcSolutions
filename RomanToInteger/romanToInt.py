class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        integer = 0
        largest = 0
        roman = iter(reversed(s))

        #want to subtract numbers when following char is less than previous
        for x in roman:
            print(x)
            if numerals[str(x)] >= largest:
                largest = numerals[str(x)]
                integer += numerals[str(x)]
            else:
                integer -= numerals[str(x)]

        return(integer)
