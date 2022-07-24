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
            return False
        
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

#adding constant solution below:

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
        try: 
            slow = head
            fast = head.next
            
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next   
            
            return True #slow IS fast, cycle detected
        
        except:# fast.next.next became Null, end of list with no cycle
            return False
