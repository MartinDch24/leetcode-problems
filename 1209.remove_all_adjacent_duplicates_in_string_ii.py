class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # We'll use a stack to track duplicates right next to each other

        for c in s:
            if stack and stack[-1][0] == c: # If there are elements in the stack and the top character is the same as our current one
                stack[-1] = (c, stack[-1][1] + 1)   # Increment the count of the stack's top element
                if stack[-1][1] == k:   # If the count reaches k, pop the element
                    stack.pop()
            else:
                stack.append((c, 1))    # Otherwise append it with a count of 1

        return "".join(c * count for c, count in stack) # Since we don't save consecutive duplicates, but just increment the count of the specific letter, we multiply the characters left by their counts to get the actual string
