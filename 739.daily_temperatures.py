#Resolved
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []  # Store non-resolved indices (no warmer temperature yet)

        for i in range(n):
            # Iterate through all of the temperature indices for which you've currently found a warmer day
            while stack and temperatures[stack[-1]] < temperatures[i]:
                idx = stack.pop()
                answer[idx] = i-idx

            stack.append(i)

        return answer