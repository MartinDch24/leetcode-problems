#Resolved
class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        def get_neighbors(code):    # Iterate over every digit, change it by 1 and return the new code
            for i in range(4):
                digit = int(code[i])
                for move in (-1, 1):
                    new_digit = (digit + move) % 10
                    yield code[:i] + str(new_digit) + code[i+1:]

        dead = set(deadends)    # Create a set for the deadends for faster checks

        if '0000' in dead:
            return -1
        if '0000' == target:
            return 0

        start = set(['0000'])   # We will try to meet start and end in the middle, using bidirectional BFS
        end = set([target])
        visited = set(['0000'])
        steps = 0

        while start and end:
            if len(start) > len(end):   # We always expand the smaller set
                start, end = end, start

            next_level = set()  # Build a new set for start, so we go through less numbers in checks

            for code in start:
                if code in dead:
                    continue

                for neighbor in get_neighbors(code):
                    if neighbor in end: # Check if the next possible combination is already in end, i.e. start and end intersect
                        return steps + 1
                    if neighbor not in visited and neighbor not in dead:
                        visited.add(neighbor)
                        next_level.add(neighbor)

            start = next_level  # Replace start with the new set
            steps += 1

        return -1