#Resolved
from collections import deque


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root: #If we don't explicitly check for this, node will be None and when we append to the level node.val will throw an error
            return []

        q = deque([root]) #We initialize a queue to perform BFS, so we can explore level by level
        result = []

        while q:
            level = []

            for _ in range(len(q)): #By iterating through every element currently in the queue on every while iteration, we get each level
                node = q.popleft()

                level.append(node.val)

                if node.left:   #These will be able to be processed only in the next while iteration, because of the for loop having the old length of the queue as a range
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            result.append(level)

        return result