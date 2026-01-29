from collections import defaultdict
from bisect import bisect_right
class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.arr = defaultdict(list)    # {index1: (snap_id1, val1), (snap_id2, val2)...}

    def set(self, index: int, val: int) -> None:
        self.arr[index].append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        history = self.arr[index]   # The history of the value at index

        # Find the latest snap_id where the value was changed
        i = bisect_right(history, (snap_id, float('inf'))) - 1
        return history[i][1] if i >= 0 else 0



# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)