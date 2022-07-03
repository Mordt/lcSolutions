#preorder is root, left, right

"""
            1
          /   \
        2       3
      /   \
    4       5

    the above prints:
    1,2,4,5,3
"""

'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
#helper function, check if node has children
def HasChildren(root):
    if root.left is not None or root.right is not None:
            return True
    return False
class Solution:
    def PreOrder(self, root):
        #create stack, initialise curr to root
        curr = root
        stack = []

        #iterate thru
        while True:
            
            if HasChildren(curr) == True:#must not be null
                print(curr.data)
                stack.append(curr.right)
                curr = curr.left

            elif(stack):#leaf node, but stack has nodes
                print(curr.data)
                curr = stack.pop()

            else:
                break

        print()
