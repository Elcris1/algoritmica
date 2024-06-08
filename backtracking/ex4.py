# Consider n different types of stamps. We consider that each letter must carry at most m stamps being m ≤ n×3.
# Design a backtracking algorithm that finds all possible ways of stamping a letter with value V if the order of
# stamps does not matter
def backtracking(todo, m, preu, done):
    if sum(done) == preu:
        return done
    if sum(done) > preu or len(done) > m:
        return None
    
    sol = []
    for moneda in todo:
        s = backtracking(todo, m, preu, done+[moneda])
        if s:
            sol.append(s)

    return sol




monedes = [1, 2, 5, 10, 20, 50, 100, 200]
preu = 120
m = len(monedes) * 3

print(backtracking(monedes, m, preu, []))
