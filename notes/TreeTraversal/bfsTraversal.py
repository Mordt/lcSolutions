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
    def levelOrder(self, root):

        """
        algorithm:
            1. start at root, visit unvisited children. mark as visited, display, add to the queue.
            2. if no unvisited children remain, dequeue the first vertex.
            3. repeat until queue is empty or desired node is found.
        """

        curr = root
        visited, queue = []

        visited.append(curr)
        queue.append(curr)

        while True:

            curr = queue.pop(0)
            print(curr)