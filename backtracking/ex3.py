# Consider n different letters. Design a backtracking algorithm that finds all words of length m, with m < n,
# without letter repetition.
def backtracking(todo, done, m):
    if len(done) == m:
        return done
    if len(done) > m or not todo:
        return None
    
    sol = []
    for lletra in todo:
        s = backtracking([x for x in todo if x != lletra], done+[lletra], m)
        if s:
            sol.append(s)

    return sol

n = ["a", "b" , "c", "d"]
m = 2

print(backtracking(n, [], m))
