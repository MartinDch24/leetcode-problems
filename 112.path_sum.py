#Resolved

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

        s = [(root, root.val)]  #We use a stack for a DFS solution. In it, we save the node and the sum so far.

        while s:
            node, curr_sum = s.pop()

            if not node.left and not node.right:    # If the node is a leaf, check if the accumulated sum equals targetSum.
                if curr_sum == targetSum:           # If it does, return True; otherwise, keep searching.
                    return True
                continue

            if node.left:   #If the node has a node left of it, we append it to the stack, along with the new sum
                s.append((node.left, curr_sum + node.left.val))
            if node.right:  #If the node has a node right of it, we append it to the stack, along with the new sum
                s.append((node.right, curr_sum + node.right.val))

        return False

        #BFS solution:
        # q = deque([(root, root.val)])
        #
        # while q:
        #     for _ in range(len(q)):
        #         cur, cur_sum = q.popleft()
        #
        #         if not cur.left and not cur.right and cur_sum == targetSum:
        #             return True
        #
        #         if cur.left:
        #             q.append((cur.left, cur_sum + cur.left.val))
        #         if cur.right:
        #             q.append((cur.right, cur_sum + cur.right.val))
        #
        # return False