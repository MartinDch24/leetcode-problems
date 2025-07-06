from collections import defaultdict


class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        max_fruits = 0
        window = defaultdict(int)   # {<fruit1>: <it's count>, ....}

        left = 0
        for right in range(len(fruits)):
            window[fruits[right]] += 1  # Add a new fruit as we move along

            while len(window) > 2:  # If we have more than 2 types of fruit
                window[fruits[left]] -= 1   # Start removing from the left
                if window[fruits[left]] == 0:
                    del window[fruits[left]]    # If there is no more of this fruit, delete the key in window
                left += 1   # Increment left and continue shrinking the window

            max_fruits = max(max_fruits, right - left + 1)  # Check whether the new window is longer than the previous ones

        return max_fruits