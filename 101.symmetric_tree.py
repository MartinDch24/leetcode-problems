# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:  # We assume a None root is symmetric
            return True

        stack = [(root.left, root.right)]  # Initialize a stack with the left and right side of the root node

        while stack:  # Do DFS on both sides at the same time
            l_node, r_node = stack.pop()

            if not l_node and not r_node:  # If both nodes are None, then we still have symetry
                continue
            if not l_node or not r_node:  # If only one node is None, then symetry is broken
                return False

            if l_node.val != r_node.val:  # If the values mismatch, then it's not symmetrical
                return False

            stack.append((l_node.left,
                          r_node.right))  # Since it's supposed to be mirrored we take the left side of the left node and pair it with the right side of the right node
            stack.append((l_node.right, r_node.left))

        return True