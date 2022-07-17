# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #will modify from maxdepth by returning as soon as we see a not curr.left/right
        if root == None:
            return 0
        
        level = 1
        queue = []
        queue.append(root)
        
        while(queue):
            
            levelSize = len(queue)
            while(levelSize != 0):#level order algo here
                
                curr = queue.pop(0)
                if curr.left:
                    queue.append(curr.left)
                else:
                    return level
                
                if curr.right:
                    queue.append(curr.right)
                else:
                    return level
                
                levelSize -= 1
            
            level += 1

        #return level


