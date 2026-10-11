class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        n = len(nums)
        i = 0
        visited = set()
        for j in range(n):
            while j - i > k:
                visited.remove(nums[i])
                i += 1

            if nums[j] in visited:
                return True
            visited.add(nums[j])

        return False
