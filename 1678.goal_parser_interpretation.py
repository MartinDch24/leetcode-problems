class Solution:
    def interpret(self, command: str) -> str:
        strings = {'G': 'G', '()': 'o', '(al)': 'al'}   # Strings and their parsed versions
        curr_command = ""   # The string we have built up from the characters in the command so far
        res = ""    # The total result of parsed strings

        for c in command:
            curr_command += c   # Add the current character to the current command string
            if curr_command in strings:
                res += strings[curr_command]    # Parse the string and add it to result
                curr_command = ""   # Clear the current command string

        return res