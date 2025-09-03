class Solution:
    def isHappy(self, n: int) -> bool:
        uniques = set() # Set for cycle detection

        digit_sum = 0   # The sum of the digits in the current number
        while n != 1:
            while n:
                digit = n % 10  # Take the last digit of n
                digit_sum += digit ** 2 # Square it and add it to the sum
                n //= 10    # Remove the last digit of n

            if digit_sum in uniques:    # If we have had the number before, then we've entered a loop
                return False
            uniques.add(digit_sum)

            n = digit_sum   # Make n the digit sum and zero the sum
            digit_sum = 0

        return True