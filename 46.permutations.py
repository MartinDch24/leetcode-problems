class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        used = [False] * n
        res = []

        def backtrack(path):
            if len(path) == n:
                res.append(path[:])
                return

            for i in range(n):
                if used[i]:
                    continue

                path.append(nums[i])
                used[i] = True
                backtrack(path)
                path.pop()
                used[i] = False
        backtrack([])
        return res