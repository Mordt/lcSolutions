# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: none
        """
        if root is None:
            return False

        queue = []
        curr = root
        queue.append(curr)
        level = 0
        
        #map to track nodes -> (parent, depth)
        nodeMap = {}
        nodeMap[curr.val] = (None, level)
        if curr.left:
            level += 1
            nodeMap[curr.left.val] = (curr.val, level)
            level -= 1
        if curr.right:
            level += 1
            nodeMap[curr.right.val] = (curr.val, level)
            level -= 1
        
        while len(queue) > 0:
            found = False
            
            levelSize = len(queue)
            while(levelSize != 0):
                
                curr = queue.pop(0)
                
                if curr.left:
                    queue.append(curr.left)
                    level += 1
                    nodeMap[curr.left.val] = (curr.val, level)
                    level -= 1
                if curr.right:
                    queue.append(curr.right)
                    level += 1
                    nodeMap[curr.right.val] = (curr.val, level)
                    level -= 1
                
                levelSize -= 1
            
            if found:
                break
            level += 1
            
        #print("x is: ", x, nodeMap.get(x)[0])
        #checking if map works
        nodeParent = nodeMap.get(x)[0]
        nodeDepth = nodeMap.get(x)[1]
        
        for key in nodeMap:
            keyParent = nodeMap.get(key)[0]
            keyDepth = nodeMap.get(key)[1]
            
            if keyParent != nodeParent and keyDepth == nodeDepth:
                print(key)
                      

