class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        targets = {num: -1 for num in nums1}    # {num1: <its next greater element>,
                                                # num2: <its next greater element>, ...etc}

        stack = []  # Save the indices of unresolved elements
        for j in range(n):
            # Check if nums2[j] is greater than any of the unresolved elements
            while stack and nums2[stack[-1]] < nums2[j]:
                idx = stack.pop()

                # If nums2[idx] is a part of nums1, we save nums2[j] as its next greater element
                if nums2[idx] in targets:
                    targets[nums2[idx]] = nums2[j]

            stack.append(j)

        return [targets[num] for num in nums1]