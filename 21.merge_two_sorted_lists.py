class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode() # dummy.next will be the result and this is an empty instance so we can keep the head
        curr = dummy    # Node depth so far

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1   # The following node because the one with the larger value
                list1 = list1.next  # We move the given list forward
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next    # Move the current node forward

        if list1:   # This check protects us from both empty input and the case where one list ends before the other
            curr.next = list1   # We don't need to iterate through it, just attach the head
        elif list2:
            curr.next = list2

        return dummy.next