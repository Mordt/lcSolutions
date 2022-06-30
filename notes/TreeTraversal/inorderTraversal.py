class Solution:
    def InOrder(self,root):
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
        nodeStack.insert(0,curr)
        while curr != null:
            
            curr = curr.left
        
        #curr == null
        if len(nodeStack) != 0:#if stack not empty
            popped = nodeStack.pop(0)
            print(popped)
            curr = popped.right