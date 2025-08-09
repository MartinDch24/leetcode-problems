class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()   # Convert uppercase characters to lowercase
        res = "".join(char for char in s if char.isalnum()) # Take all characters that are alphanumeric and join them without a space

        return res == res[::-1] # Compare the string to it's reversed state