class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def backtrack(start, path):
            res.append(path[:]) # Add our current path as a valid subset

            for i in range(start, n):
                path.append(nums[i])    # Choose to take element

                backtrack(i+1, path)    # Explore paths deeper

                path.pop()  # Exclude element from future paths

        backtrack(0, [])
        return res