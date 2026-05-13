class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []

        def backtrack(start, path, total):
            if total == target:
                res.append(path[:])
                return
            elif total > target:
                return

            for i in range(start, n):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                # Array is sorted, so it would be pointless to iterate further
                if total + candidates[i] > target:
                    break

                path.append(candidates[i])
                backtrack(i+1, path, total + candidates[i])
                path.pop()

        backtrack(0, [], 0)
        return res