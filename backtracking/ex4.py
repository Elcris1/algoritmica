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


def branchandbound(todo, m, preu, done, best):
    if sum(done) == preu:
        return done
    if sum(done) > preu or len(done) > m:
        return None
    if len(done) > len(best):
        return best
    
    for moneda in todo:
        s = branchandbound(todo, m, preu, done+[moneda], best)
        if s and len(s) < len(best):
            best = s

    return best

monedes = [1, 2, 5, 10, 20, 50, 100, 200]
preu = 120
m = len(monedes) * 3

#print(backtracking(monedes, m, preu, []))
print(branchandbound(monedes, m, preu, [], [x for x in range(preu)]))
