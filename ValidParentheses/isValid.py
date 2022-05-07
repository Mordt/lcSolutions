class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #quick function to look at top of a stack
        def peekStack(stack):
            if stack:
                return stack[-1]
            else:
                return None

        stack = []
        for x in s:
            if x == '(' or x == '[' or x == '{':
                stack.append(x)

            elif x == ')' or x == ']' or x == '}':
                y = peekStack(stack)
                if x == ')' and y == '(':
                    stack.pop()
                elif x == ']' and y == '[':
                    stack.pop()
                elif x == '}' and y == '{':
                    stack.pop()
                else:
                    stack.append(x)

        if not stack:
            return True
        else:
            return False

    #this was my own solution, however it seems as though neetcodes is similar just with a hashmap
    #easier to check the stack tbh
    #neetcode below

    """
    Map = { ")":"(", "]":"[", "}":"{" }
        stack = []
        
        for c in s:
            if c not in Map:
                stack.append(c)
                continue    
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()
            
        return not stack
    """