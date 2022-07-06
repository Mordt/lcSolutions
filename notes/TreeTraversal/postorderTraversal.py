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
            #if

            #elif

            #else