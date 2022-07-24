# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        #create "visited set"
        if head == None:
            return None
        
        visited = set()
        while head is not None:
            if head in visited:
                return head #cycle discovered
            else:
                #add to visited
                visited.add(head)
                head = head.next
        #only here if reach end of list and not cycle
        return None # not a cycle
