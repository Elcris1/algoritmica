activitats = [x + 1 for x in range(8)]
calories = [1000, -500, 200, -300, -200, 50, -3000, 250]
preu = [15, 0, 10, 5, 0, 3, 20, 5]


def backtracking(todo, calories, done = []):
    if len(done) != 0 and sumacalories(done, calories) == 0:
        done.sort()
        print(done)
        return done
    if not todo:
        return None
    
    sol = []
    for act in todo:
        s = backtracking([x for x in todo if x != act], calories, done + [act])
        if s and s not in sol:
            sol += [s]
    return sol

def sumacalories(done, calories):
    sum = 0
    for elemen in done:
        sum += calories[elemen-1]
    return sum
print(backtracking(activitats, calories))