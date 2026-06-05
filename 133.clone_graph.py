#Resolved
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        copy = {node: Node(val=node.val)}
        s = [node]

        while s:
            curr_node = s.pop()

            for n in curr_node.neighbors:
                # Track already processed nodes
                if n not in copy:
                    copy[n] = Node(val=n.val)
                    s.append(n)

                # Connect neighbors
                copy[curr_node].neighbors.append(copy[n])

        return copy[node]