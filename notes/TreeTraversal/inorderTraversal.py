#inorder is left, root, right
"""
            1
          /   \
        2       3
      /   \
    4       5

    the above prints:
    4,2,5,1,3
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
    def InOrder(self, root):
        # code here

        #create stack for iterative traversal
        """
        1) Create an empty stack S.
        2) Initialize current node as root
        3) Push the current node to S and set current = current->left until current is NULL
        4) If current is NULL and stack is not empty then 
             a) Pop the top item from stack.
             b) Print the popped item, set current = popped_item->right 
             c) Go to step 3.
        5) If current is NULL and stack is empty then we are done.
        """
        nodeStack = []
        curr = root

        while True:
            if curr is not None:
                nodeStack.append(curr)
                curr = curr.left

            #curr == null
            elif(nodeStack):  # if stack not empty
                curr = nodeStack.pop()
                print(curr.data, end = " ")
                curr = curr.right

            else:
                break

        print()

        """
        #inorder traversal is left, root, right
        current = root
        stack = [] # initialize stack
         
        while True:
            # Reach the left most Node of the current Node
            if current is not None:
                # Place pointer to a tree node on the stack
                # before traversing the node's left subtree
                stack.append(current)
                current = current.left

            # BackTrack from the empty subtree and visit the Node
            # at the top of the stack; however, if the stack is
            # empty you are done
            elif(stack):#if stack not empty
                current = stack.pop()
                print(current.data, end=" ") # Python 3 printing
             
                # We have visited the node and its left
                # subtree. Now, it's right subtree's turn
                current = current.right
     
            else:
                break
          
        print()

        """

#recursive solution:
# A function to do inorder tree traversal
def printInorder(root):

    if root:

        # First recur on left child
        printInorder(root.left)

        # then print the data of node
        print(root.val),

        # now recur on right child
        printInorder(root.right)
