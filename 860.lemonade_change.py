#Resolved
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0   # 5 and 10 dollar bills
        tens = 0

        for b in bills:
            if b == 5:  # All 5s go to change
                fives += 1
            elif b == 10:   # For each 10, we have to return a 5
                if fives:
                    fives -= 1
                    tens += 1
                else:   # If we don't have any 5s, we can't give change
                    return False

            else:
                # For 20s, we either return 5 + 10 or 5*3
                if tens and fives:
                    tens -= 1
                    fives -= 1
                elif fives >= 3:
                    fives -= 3
                else:
                    return False

        return True