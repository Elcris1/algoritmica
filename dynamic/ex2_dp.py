"""
(Knapsack Problem:) Given a set of items, each with a weight and a value, determine the maximum value that
can be obtained by selecting a subset of items that fit into a knapsack of limited capacity
"""

def funcio(items, values, pesos, capacitat):
    memo = [[0 for x in range(capacitat+1)] for x in range(len(items)+1)]

    for i in range(len(items) + 1):
        for j in range(capacitat + 1):
            """
            restant = capacitat actual - pes
            memo[i][j] = max (valor anterior, valor item actual + memo[item actual - 1][restant])
            """
            if i == 0 or j == 0:
                memo[i][j] = 0
            # si cap el item (agafo maxim de fila anterior o la suma del item actual + valor item amb el pes restant)
            elif (pesos[i - 1] <= j):
                restant = j - pesos[i - 1]
                memo[i][j] = max(memo[i - 1][j], values[i - 1] + memo[i - 1][restant])
            # si no hi cap agafo la combinacio anterior (fila de dalt)
            else:
                memo[i][j] = memo[i - 1][j]

    return memo[len(items)][capacitat]

items = [1,2,3,4]
values = [30,14,16,9]
pesos = [6,3,4,2]
capacitat = 9

print(funcio(items, values, pesos, capacitat))