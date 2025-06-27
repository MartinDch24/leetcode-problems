# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        curr = root
        s = []
        res = []

        while s or curr:
            while curr:
                s.append(curr)
                curr = curr.left

            node = s.pop()
            res.append(node.val)

            curr = node.right

        return res