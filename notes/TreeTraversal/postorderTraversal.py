#postorder is left, right, root

"""
            1
          /   \
        2       3
      /   \
    4       5

    the above prints:
    4,5,2,3,1
"""

'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
#my attempt:
class Solution:
    def PostOrder(self, root):

        #initial ideas
        # put root on stack, then right node then process left subtree
        
        stack = []
        curr = root
        
        while True:
            if curr is not None:
                stack.append(curr)
                if curr.right is not None:
                    stack.append(curr.right)
                
                curr = curr.left

            elif(stack): #if stack not empty
                curr = stack.pop()
                print(curr.data)
                
            else:
                break 