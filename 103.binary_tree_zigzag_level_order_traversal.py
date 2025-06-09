from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []

        q = deque([root])
        res = []
        steps = 0

        while q:
            level_vals = []

            for _ in range(len(q)):
                cur = q.popleft()
                level_vals.append(cur.val)

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

            if steps % 2 != 0:
                level_vals.reverse()

            steps += 1
            res.append(level_vals)

        return res