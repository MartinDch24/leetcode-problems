class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # Order so we can skip duplicates later
        n = len(nums)
        res = []

        def backtrack(start, path):
            res.append(path[:])

            for i in range(start, n):
                # Skip duplicates at this depth level
                if i > start and nums[i-1] == nums[i]:
                    continue

                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()

        backtrack(0, [])
        return res