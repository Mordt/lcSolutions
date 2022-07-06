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
from collections import deque
class Solution:
    def PostOrder(self, root):

        #initial ideas
        # put root on stack, then right node then process left subtree
        if root is None:
            return

        stack = []
        curr = root
        
        while stack:
            if curr is not None:
                stack.append(curr)
                if curr.right is not None:
                    stack.append(curr.right)
                
                curr = curr.left

            elif(stack): #if stack not empty
                curr = stack.pop()
                print(curr.data, end = " ")
                
            else:
                break 

#correct solution:
# Iterative function to perform postorder traversal on the tree
# main idea is to iterate through and add to a "printing" stack.

def postorderIterative(root):

    if root is None:
        return

    stack = deque()
    stack.append(root)
    out = deque()  # another stack to store postorder traversal

    while stack: #loop till stack is empty

        #algorithm is stacking root, then 
        curr = stack.pop()
        out.append(curr.data)

        # push the left and right child of the popped node into the stack
        if curr.left:
            stack.append(curr.left)

        if curr.right:
            stack.append(curr.right)

    while out:
        print(out.pop(), end = " ")

"""
time and space analysis
when n is the number of nodes in tree, time comp is O(n), space comp is O(n)
"""
#postorder recursive solution
def printPostorder(root):

    if root:

        # First recur on left child
        printPostorder(root.left)

        # the recur on right child
        printPostorder(root.right)

        # now print the data of node
        print(root.val),
