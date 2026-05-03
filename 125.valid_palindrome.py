class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()   # Convert uppercase characters to lowercase
        res = "".join(char for char in s if char.isalnum()) # Take all characters that are alphanumeric and join them without a space

        return res == res[::-1] # Compare the string to it's reversed state

    # Two-pointer solution:
    # left, right = 0, len(s) - 1
    # while left < right:
    #     # Skip irrelevant characters
    #     while left < right and not s[left].isalnum():
    #         left += 1
    #     while left < right and not s[right].isalnum():
    #         right -= 1
    #
    #     if s[left].lower() != s[right].lower():
    #         return False
    #
    #     left += 1
    #     right -= 1
    #
    # return True