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
            if curr == None:
                return
            curr = queue.pop(0)
            print(curr)

            
            """
            for neighbour in graph[s]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
            """
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