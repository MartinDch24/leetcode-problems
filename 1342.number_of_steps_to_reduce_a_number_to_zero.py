#Resolved - 2
class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0

        while num:
            steps += 1

            if num % 2 == 0:
                num //= 2
            else:
                num -= 1

        return steps