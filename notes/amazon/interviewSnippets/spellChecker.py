# Implement a simple spell checker. The only requirement is that it will return true
# for words that are present in our dictionary (i.e. spelled correctly) and will return false otherwise.

def spellChecker(word, wordSet):
    #check if our word is in the dictSet
    if word in wordSet:  # only true if the spelling is the same
        return True
    else:
        return False


def createSet(wordList):
    dictSet = {}
    for x in wordList:
        dictSet.add(x)


def main(file):
    wordsSet = self.createSet(file)

    for word in file:
        <
        self.spellChecker(word, wordSet)

#time complexity: O(n+n), n is number of words in file, O(2n)

# ‘cat’ it could offer catch, caterpillar etc.


"""prestring""" [c, a, t] < | suggestions: [catch]
"""xString"""   [c, a, t, c, h]


x = "coat", xstring = [c, o, a, t]
[c, a, t]
[c, o, a, t]


def suggestor(prefix, wordSet):
    #return list of possible words starting with the prefix
    suggestions: = []
    preString = prefix.split()  # [c, a, t] instead of "cat"

    for x in wordSet:
        flag = True

        xString = x.split()
        for i, y in enumerate(preString):
            if y != xString[i]:
                << <
                flag = False
                break
        if flag:
            suggestions.add(x)  # dont add to suggestions

    return suggestions

    #time comp: if n is length of prefix, m is the length of wordSet, O(n*m)
