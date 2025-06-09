class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        pars = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in pars:
                if not stack or stack.pop() != pars[char]:
                    return False
            else:
                stack.append(char)
        return not stack