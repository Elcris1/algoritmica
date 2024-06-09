"""
(Coin Change Problem:) Given a set of coin denominations and a target amount, find the minimum number of
coins required to make up that amount.
"""

def coin_change(coins, amount):
    """
    restant = amount actual - moneda actual				
    min( anterior , anterior + memo[i - 1][restant])
    """
    memo = [[0 for x in range(amount + 1)] for x in range(len(coins) + 1)]

    for i in range(len(coins) + 1):
        for j in range(amount + 1):
            if i == 0 or j == 0:
                memo[i][j] == 0
            elif j - coins[i - 1] >= 0:
                restant = j - coins[i - 1]
                if min(memo[i - 1][j], 1 + memo[i - 1][restant]) == 0:
                    memo[i][j] = 1 + memo[i][restant]
                else:
                    memo[i][j] = min(memo[i - 1][j], 1 + memo[i][restant])
            else:
                memo[i][j] = memo[i - 1][j]

    return memo[len(coins)][amount]

coins = [1,2,5,10,20,50]
amount = 120

print(coin_change(coins, amount))