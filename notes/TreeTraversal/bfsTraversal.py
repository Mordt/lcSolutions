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

class Solution:
    def LevelOrder(self, root):

        """
        algorithm:
            1. start at root, visit unvisited children. mark as visited, display, add to the queue.
            2. if no unvisited children remain, dequeue the first vertex.
            3. repeat until queue is empty or desired node is found.
        """
        if root is None:
            return

        curr = root
        visited, queue = []

        visited.append(curr)
        queue.append(curr)

        while True:
            curr = queue.pop(0)
            print(curr)

            if curr.left is not None:
                queue.append(curr.left)
            
            if curr.right is not None:
                queue.append(curr.right)

        print()


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


def printLevel(root, level):

    # base case
    if root is None:
        return False

    if level == 1:
        print(root.key, end=' ')

        # return true if at least one node is present at a given level
        return True

    left = printLevel(root.left, level - 1)
    right = printLevel(root.right, level - 1)

    return left or right


# Function to print level order traversal of a given binary tree
def levelOrderTraversal(root):

    # start from level 1 — till the height of the tree
    level = 1

    # run till printLevel() returns false
    while printLevel(root, level):
        level = level + 1
