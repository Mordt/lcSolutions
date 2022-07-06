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
from collections import deque
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

#online soln
# Iterative function to perform inorder traversal on the tree


def inorderIterative(root):

    stack = deque()
    curr = root

    # if the current node is None and the stack is also empty, we are done
    while stack or curr:

        # if the current node exists, push it into the stack (defer it)
        # and move to its left child
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            # otherwise, if the current node is None, pop an element from the stack,
            # print it, and finally set the current node to its right child
            curr = stack.pop()
            print(curr.data, end=' ')

            curr = curr.right

#recursive solution
# A function to do preorder tree traversal
def printPreorder(root):

    if root:

        # First print the data of node
        print(root.val),

        # Then recur on left child
        printPreorder(root.left)

        # Finally recur on right child
        printPreorder(root.right)
