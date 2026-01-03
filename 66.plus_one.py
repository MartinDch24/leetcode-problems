class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1 # Start at the last digit

        # Make all 9s into 0s and carry 1 over
        while i >= 0 and digits[i] == 9:
            digits[i] = 0
            i -= 1

        # If i == -1, then the first digit was a 9 and we need to add an extra leading 1
        if i < 0:
            return [1] + digits

        # Increment the digit after all the 9s
        digits[i] += 1

        return digits