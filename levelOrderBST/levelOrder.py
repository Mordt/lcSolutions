# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #level order needs a queue, a curr
        if root is None:
            return None
        
        curr = root
        queue = []
        queue.append(curr)
        
        printList = []
        
        
        level = 0
        
        while len(queue) != 0:
            
            levelList = []
            levelSize = len(queue)
            while levelSize != 0:
            
                curr = queue.pop(0)
                levelList.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                
                levelSize -= 1
            
            printList.append(levelList)
            level += 1
        
        return printList


