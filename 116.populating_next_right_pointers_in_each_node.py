from collections import deque


# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root

        q = deque([root])

        while q:
            right_node = None

            for _ in range(len(q)):
                cur = q.popleft()

                if right_node:
                    cur.next = right_node

                right_node = cur

                if cur.left:
                    q.append(cur.right)
                    q.append(cur.left)

        return root