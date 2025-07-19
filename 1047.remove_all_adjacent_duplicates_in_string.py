class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = [] # We use a stack to check for duplicates by peeking the top of the stack on every iteration

        for char in s:
            if stack and stack[-1] == char: # If the new character is a duplicate, remove both it (by never adding it) and it's duplicate
                stack.pop()
            else:
                stack.append(char)  # Otherwise just save the chracter

        return "".join(c for c in stack)    # Since the stack is essentially a list, we convert it back to a string