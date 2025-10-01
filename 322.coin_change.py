#Resolved
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coins = [float("inf")] * (amount+1) # The minimum nuber of coins needed for every amount up to the given one
        min_coins[0] = 0    # We set the amount of 0 to 0 coins needed

        for i in range(amount+1):
            for c in coins:
                # If the current coin isn't larger in value then the amount we want, we look for the minimum amount of coins needed to get i minus the current coin
                # We will either have precomputed the value earlier or it will just be float("inf")
                # After we get the minimum coins needed for amount i-c, we add 1, which is the new coin, needed to get amount i
                if i - c >= 0:
                    min_coins[i] = min(min_coins[i], min_coins[i-c] + 1)

        # We either managed to get amount with the given coins or it remained float("inf")
        return -1 if min_coins[amount] == float("inf") else min_coins[amount]

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