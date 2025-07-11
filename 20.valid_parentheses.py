#Resolved
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pars = {'}': '{', ']': '[', ')': '('}
        stack = []  # We use a stack to track all opening parentheses so far

        for c in s:
            if c in pars:
                if not stack or stack.pop() != pars[c]:  # When we find a closing parenthese, we check whether the top of our stack is a corresponding opening parenthese
                    return False  # If we find a closing parenthese and the stack is empty or its top is not the right opening one, we return False
            else:
                stack.append(c)  # We add opening parentheses to the stack

        return not stack  # If the stack is empty, all parentheses are closed, otherwise - they're not