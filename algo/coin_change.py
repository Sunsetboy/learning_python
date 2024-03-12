from typing import List

class Solution:

    def coinChangeGreedy(self, coins: List[int], amount: int) -> int:        
        if amount == 0:
            return 0

        coins_sorted = sorted(coins)
        coins_required = 0
        rest_amount = amount
        current_coin_index = len(coins_sorted)-1
        print(f"coins: {coins_sorted}")
        while rest_amount > 0 and current_coin_index >= 0:
            if rest_amount // coins_sorted[current_coin_index]:
                print(f"{rest_amount // coins_sorted[current_coin_index]} coins of {coins_sorted[current_coin_index]}")
                coins_required += rest_amount // coins_sorted[current_coin_index]
                rest_amount = rest_amount % coins_sorted[current_coin_index]
            current_coin_index -= 1
            print(f"{rest_amount=}, {current_coin_index=}")

        if current_coin_index < 0 and rest_amount > 0:
            return -1
        
        return coins_required

    def coinChangeDP(self, coins: List[int], amount: int) -> int: 
        exchanges = [0] + ([float('inf')]*amount)

        for i in range(1, amount+1):
            for coin in coins:
                if coin <= i:
                    exchanges[i] = min(exchanges[i], exchanges[i-coin]+1)
        if exchanges[-1] == float('inf'):
            return -1
        return exchanges[-1]
    
def main():
    solution = Solution()
    print(solution.coinChangeGreedy([1,2,5], 11))
    print(solution.coinChangeDP([1,2,5], 11))


if __name__ == "__main__":
    main()