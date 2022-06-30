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

from distutils.command.sdist import sdist
from turtle import setundobuffer


class Solution:
    
    #helper function, check if node has children
    def HasChildren(self, root):
        if root.left is not None and root.right is not None:
            return True
        return False

    def PreOrder(self, root):

        #create stack, initialise curr to root
        curr = root
        stack = []

        #iterate thru
        while True:

            if curr is not None:
                #

            elif(stack):
                #more stuff

            else:
                break

        print()
