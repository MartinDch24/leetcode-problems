class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0

        stack = []  # Store indices of elements in a non-decreasing order
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                idx = stack.pop()

                # arr[idx] is the smallest number up to stack[-1] on the left
                # and i on the right
                # left and right are the distances from idx to those indices
                left = idx - stack[-1] if stack else idx + 1
                right = i - idx

                # Every subarray we can form comes from every possible start on left,
                # multiplied by every possible end on the right
                # and finally we multiply  by arr[idx], because it will be the smallest element in all of those subarrays
                res += arr[idx] * left * right
            stack.append(i)

        # Some elements might remain in the stack
        # For them, they are the smallest from idx to n
        while stack:
            idx = stack.pop()
            left = idx - stack[-1] if stack else idx + 1
            right = n - idx
            res += arr[idx] * left * right

        return res % (10 ** 9 + 7)