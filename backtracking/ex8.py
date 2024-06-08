#grap coloring
def backtracking(todo, done: dict, graph):
    if not todo:
        #print(done)
        return done
    
    sol = []
    for node in todo:
        for color in colors:
            if valid(color, node, done):
                done[node] = color
                s = backtracking([x for x in todo if x != node], done, graph)
                sol += [s]
    return sol


def valid(color, node, done):
    adjacents = graph[node]
    for nod in adjacents:
        if done[nod] == color:
            return False
    return True

def branchandbound(todo, done: dict, graph, best):
    if not todo:
        return done
    if lb(todo, done) >= contarColors(best):
        return best
    
    for node in todo:
        for color in colors:
            if valid(color, node, done):
                done[node] = color
                s = branchandbound([x for x in todo if x != node], done, graph, best)
                if contarColors(s) < contarColors(best):
                    best = s
    return best

def lb(todo, done):
    return contarColors(done)

def contarColors(dict: dict):
    count = 0
    colors = []
    for color in dict.values():
        if color not in colors:
            colors.append(color)
            count += 1

    return count

graph = {}   
graph['A'] = ['B', 'D', 'C']
graph['B'] = ['C', 'A']
graph['C'] = ['A', 'B']
graph['D'] = ['A']

colors = ["RED", "BLUE", "GREEN", "YELLOW"]

#print(backtracking(['A', 'B', 'C', 'D'], {"A":None, "B": None, "C": None, "D": None}, graph))
print(branchandbound(['A', 'B', 'C', 'D'], {"A":None, "B": None, "C": None, "D": None}, graph, {"A":"RED", "B": "BLUE", "C": "GREEN", "D": "YELLOW"}))
