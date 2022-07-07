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
        self.val = val
        self.left = None
        self.right = None
'''


class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        if root is None:
            return False

        #keep track of level
        queue = deque()
        curr = root
        queue.append(curr)
        level = 0

        while len(queue) > 0:

            levelSize = len(queue)

            while(levelSize != 0):

                curr = queue.pop()
                print(curr.val, level)

                if curr.left:
                    queue.append(curr.left)

                if curr.right:
                    queue.append(curr.right)

                levelSize -= 1

            level += 1

        return False


"""
    def bfs(self, root=None):
        if root is None:
            return
        queue = [root]

        while len(queue) > 0:
            cur_node = queue.pop(0)

            if cur_node.left is not None:
                queue.append(cur_node.left)

            if cur_node.right is not None:
                queue.append(cur_node.right)

            print(queue)

"""

#recursive solution
# Function to print all nodes of a given level from left to right
# Function to print level order traversal of a given binary tree

from collections import deque
def levelOrderTraversal(root):

    # base case
    if not root:
        return

    # create an empty queue and enqueue the root node
    queue = deque()
    queue.append(root)

    # loop till queue is empty
    while queue:

        # process each node in the queue and enqueue their
        # non-empty left and right child
        curr = queue.popleft()

        print(curr.key, end=' ')

        if curr.left:
            queue.append(curr.left)

        if curr.right:
            queue.append(curr.right)
