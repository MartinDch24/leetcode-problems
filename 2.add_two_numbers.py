
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        first_num = 0
        second_num = 0
        result = ListNode(0)

        counter = 0
        while l1:
            first_num += l1.val * 10 ** counter
            l1 = l1.next

        counter = 0
        while l2:
            second_num += l2.val * 10 ** counter
            l2 = l2.next

        sum = first_num + second_num

        current_node = result
        while sum:
            new_node = ListNode(sum % 10)
            current_node.next = new_node
            current_node = new_node
            sum//=10

        return result.next