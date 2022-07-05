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

class Solution:
    def PostOrder(self, root):

        #initial ideas
        #wanna put root on stack, then right node then 
        #print left node if it's a leaf