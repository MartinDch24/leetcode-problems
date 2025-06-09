from sortedcontainers import SortedList

class Solution(object):
    def maxTaskAssign(self, tasks, workers, pills, strength):
        """
        :type tasks: List[int]
        :type workers: List[int]
        :type pills: int
        :type strength: int
        :rtype: int
        """
        tasks.sort()
        workers.sort()

        def can_complete_tasks(x):
            remaining_pills = pills
            easiest_tasks = tasks[:x]
            strongest_workers = SortedList(workers[-x:])

            for i in range(x-1, -1, -1):
                task = easiest_tasks[i]
                if strongest_workers and strongest_workers[-1] >= task:
                    strongest_workers.pop()

                else:
                    idx = strongest_workers.bisect_left(task - strength)
                    if idx == len(strongest_workers):
                        return False

                    strongest_workers.pop(idx)
                    remaining_pills -= 1

                    if remaining_pills < 0:
                        return False
            return True

        right = min(len(tasks), len(workers))
        left = 0
        answer = 0

        while left <= right:
            mid = (left + right) // 2
            if can_complete_tasks(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer
