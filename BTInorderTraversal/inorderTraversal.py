# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if root is None:
            return None
        
        stack = []
        curr = root
        inorder = []
        
        while True:
            #if curr is not null, add to stack
            #keep going till end is reached
            if curr is not None:
                stack.append(curr)
                curr = curr.left
            
            elif(stack):#if current is null and stack is not empty
                #pop stack, print and go right
                curr = stack.pop()
                #print(curr.val)
                inorder.append(curr.val)
                curr = curr.right
            else:
                break
        
        return inorder




