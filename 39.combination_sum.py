class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []

        def backtrack(start, path, total):
            if total == target:
                res.append(path[:])
                return

            if total > target:
                return

            for i in range(start, n):
                if total + candidates[i] > target:
                    break

                path.append(candidates[i])
                # We put i as the value for start, because reusing is allowed
                backtrack(i, path, total + candidates[i])
                path.pop()

        backtrack(0, [], 0)
        return res