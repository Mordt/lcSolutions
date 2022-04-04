# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #have last num
        #if currnum == lastnum, delete currnum
        if head == None:
            return head

        currNum = head.val
        head = head.next

        while head != None:
            print head.val
            if head.val == currNum:
                #delete node, move on
            else:  # update current number, proceed
                currNum = head.val
                head = head.next
