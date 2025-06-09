from collections import deque


# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None

        clones = {}

        clones[node] = Node(node.val)
        queue = deque([node])

        while queue:
            curr = queue.popleft()
            curr_neighbors = []

            for neighbor in curr.neighbors:
                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                curr_neighbors.append(clones[neighbor])
            clones[curr].neighbors = curr_neighbors

        return clones[node]