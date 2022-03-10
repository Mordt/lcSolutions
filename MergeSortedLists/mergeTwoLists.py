# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #checking edge cases lists empty
        if list1 == None and list2 == None:
            return None
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        #track current position in lists
        retl = ListNode()
        track1 = ListNode()
        track2 = ListNode()

        while retl != None:
            if track1 == None:
                #stuff
            if track2 == None:
                #stuff

            if list1.value < list2.value:
                retl = list1
                retl.next

            retl = retl.next
