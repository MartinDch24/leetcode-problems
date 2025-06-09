from collections import deque


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False

        q = deque([(root, root.val)])

        while q:
            for _ in range(len(q)):
                cur, cur_sum = q.popleft()

                if not cur.left and not cur.right and cur_sum == targetSum:
                    return True

                if cur.left:
                    q.append((cur.left, cur_sum + cur.left.val))
                if cur.right:
                    q.append((cur.right, cur_sum + cur.right.val))

        return False


        # s = [(root, root.val)]
        #
        # while s:
        #     cur, cur_sum = s.pop()
        #
        #     if not cur.left and not cur.right and cur_sum == targetSum:
        #         return True
        #
        #     if cur.right:
        #         s.append((cur.right, cur_sum + cur.right.val))
        #     if cur.left:
        #         s.append((cur.left, cur_sum + cur.left.val))
        #
        # return False