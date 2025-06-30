# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0

        stack = [(root, False)]  # (node, visited)
        depth = {}               # node: depth
        diameter = 0

        while stack:
            node, visited = stack.pop()

            if not node:
                continue

            if visited:
                left_depth = depth.get(node.left, 0)
                right_depth = depth.get(node.right, 0)

                # Update the diameter
                diameter = max(diameter, left_depth + right_depth)

                # Save the depth of this node
                depth[node] = 1 + max(left_depth, right_depth)
            else:
                # Push the node back to the stack, it's right and left node along with it
                stack.append((node, True))

                stack.append((node.right, False))
                stack.append((node.left, False))

        return diameter