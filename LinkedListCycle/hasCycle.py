# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #assume nodes aren't repeated.
        #create "visited set"
        if head == None:
            return True
        
        visited = set()
        while head is not None:
            if head in visited:
                return True #cycle discovered
            else:
                #add to visited
                visited.add(head)
                head = head.next
        #only here if reach end of list and not cycle
        return False # not a cycle

