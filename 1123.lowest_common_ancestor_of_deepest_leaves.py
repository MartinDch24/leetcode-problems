class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """

        def findMaxDepth(node, depth=0):
            if node is None:
                return depth

            l = findMaxDepth(node.left, depth + 1)
            r = findMaxDepth(node.right, depth + 1)

            return max(l, r)

        max_depth = findMaxDepth(root)

        def lowestCommonAncestor(node, depth=0, max_depth=0):
            if node is None:
                return node

            if depth == max_depth:
                return node

            l = lowestCommonAncestor(node.left, depth + 1, max_depth)
            r = lowestCommonAncestor(node.right, depth + 1, max_depth)

            if l and r:
                return node

            return l if l else r

        return lowestCommonAncestor(root, 0, max_depth - 1)

        # def dfs(node):
        #     if not node:
        #         return (0, None)  # (depth, LCA)
        #
        #     left_depth, left_lca = dfs(node.left)
        #     right_depth, right_lca = dfs(node.right)
        #
        #     if left_depth > right_depth:
        #         return (left_depth + 1, left_lca)
        #     elif right_depth > left_depth:
        #         return (right_depth + 1, right_lca)
        #     else:
        #         return (left_depth + 1, node)  # Both sides are equal, so current node is LCA
        #
        # return dfs(root)[1]