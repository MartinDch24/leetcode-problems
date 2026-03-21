from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curr_sum = 0
        prefix = defaultdict(int)   # {<sum>: <how many times it appears>}
        prefix[0] = 1   # If curr_sum == k, we need to have counted it

        for num in nums:
            curr_sum += num

            # curr_sum - <sum of elements before the subarray> == k
            # When we rearrange it, we get curr_sum - k == <sum of elements before the subarray>
            res += prefix[curr_sum - k]

            prefix[curr_sum] += 1

        return res