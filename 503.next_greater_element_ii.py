class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n

        stack = []  # Indices of strictly decreasing nums
        # Iterate twice to wrap around and go from the last index back to the first
        for i in range(n * 2):
            while stack and nums[stack[-1]] < nums[i % n]:
                idx = stack.pop()
                # Assign the next greater num to the index of every element
                res[idx] = nums[i % n]
            # Append indices only on the first loop, so we don't repeat for already resolved ones
            if i < n:
                stack.append(i)

        return res