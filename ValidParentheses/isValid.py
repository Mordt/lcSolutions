class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #quick function to look at top of stack
        #adding comments for clarity
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
