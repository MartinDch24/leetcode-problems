class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        fuel = 0  # Current fuel
        start = 0  # Starting index

        for i in range(n):
            fuel += gas[i] - cost[i]  # Fill up and subtract the cost of going to the station

            # If the fuel becomes negative, all starting indices up to this point are invalid
            if fuel < 0:
                fuel = 0  # Reset fuel
                start = i + 1  # Try to start from the next gas station

        # Before returning start, check if there even is enough gas to make the trip
        return start if sum(gas) >= sum(cost) else -1