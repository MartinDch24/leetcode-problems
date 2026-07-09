#Resolved - 2
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        # dp[i] = min coins to get amount i
        dp = [float("inf")] * (amount+1)
        dp[0] = 0

        for i in range(1, amount+1):
            for c in coins:
                # Skip coins larger than the current amount
                # Since the list is sorted, we can exit early
                if c > i:
                    break
                dp[i] = min(dp[i], dp[i-c] + 1)
        
        return dp[amount] if dp[amount] != float("inf") else -1

    #BFS solution:

        # if amount == 0:
        #     return 0
        #
        # q = deque([(0, 0)])  # Start with a sum of zero, along with 0 coins
        # visited = {0}  # The sum of 0 is already visited
        #
        # while q:
        #     curr_sum, curr_coins = q.popleft()
        #
        #     for c in coins:
        #         new_sum = curr_sum + c  # Add each coin to the current sum
        #
        #         # If the new sum is equal to amount we found the min coins needed
        #         if new_sum == amount:
        #             return curr_coins + 1
        #
        #         # If we have already visited the sum before or it is greater than amount, there's no point putting it in the queue
        #         if new_sum < amount and new_sum not in visited:
        #             visited.add(new_sum)
        #             q.append((new_sum, curr_coins + 1))
        #
        # return -1