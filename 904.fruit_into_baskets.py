#Resolved
from collections import defaultdict


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_count = defaultdict(int)  # {fruit: <how many times it appears in the current window>, ...}
        left = 0
        max_fruits = 0

        for right, fruit in enumerate(fruits):
            fruit_count[fruit] += 1

            # While we have more than 2 unique fruits,
            # Keep removing from the left, until only 2 unique ones are left
            while len(fruit_count) > 2:
                fruit_count[fruits[left]] -= 1

                if fruit_count[fruits[left]] == 0:
                    del fruit_count[fruits[left]]

                left += 1

            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits