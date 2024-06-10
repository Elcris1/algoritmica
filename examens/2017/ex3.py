activitats = [x + 1 for x in range(8)]
calories = [1000, -500, 200, -300, -200, 50, -3000, 250]
preu = [15, 0, 10, 5, 0, 3, 20, 5]
c = 500

def suma(done, calories):
    sum = 0
    for elemen in done:
        sum += calories[elemen-1]
    return sum


def backtracking(todo, c, preu, calories,  best, done = []):
    if len(done) > 10:
        return None
    if suma(done, calories) == c:
        return done
    if suma(done, preu) > suma(best, preu):
        return best
    
    for elem in todo:
        s = backtracking(todo, c, preu, calories, best, done + [elem] )
        if s and suma(s, preu) < suma(best, preu):
            best = s
    return best

print(backtracking(activitats, c, preu, calories, activitats))