activitats = [x for x in range(9)]
calories = [1000, -500, 200, -300, -200, 50, -3000, 250]
preu = [15, 0, 10, 5, 0, 3, 20, 5]
m = 3

def greedy(calories: list, m):
    sol = []
    for i in range(m):
        index = calories.index(min(calories))
        sol.append(index+1)
        calories[index] = 900000000000000

    return sol

print(greedy(calories, m))
