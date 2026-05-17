class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        used = [False] * n  # Track numbers, already in the permutation
        res = []

        def backtrack(path):
            if len(path) == n:
                res.append(path[:])
                return

            for i in range(n):
                # Skip duplicates branches:
                # - Only use nums[i] if the previous duplicate is already used
                if i > 0 and nums[i - 1] == nums[i] and not used[i - 1]:
                    continue

                if used[i]:
                    continue

                path.append(nums[i])
                used[i] = True
                backtrack(path)
                path.pop()
                used[i] = False

        backtrack([])
        return res