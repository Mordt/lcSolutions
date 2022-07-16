# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #classic level order traversal
        #keep track of level as u go
        if root == None:
            return 0
        
        level = 0
        queue = []
        queue.append(root)
        
        while(queue):
            
            levelSize = len(queue)
            while(levelSize != 0):#level order algo here
                
                curr = queue.pop(0)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                levelSize -= 1
            
            level += 1

        return level
                
                
         
