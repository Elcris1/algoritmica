# Given a graph with possible cycles, design an algorithm to find the maximum path between nodes in the graph
# (the path does not contain any cycle).
def backtrack(done: list, todo: list, next):
    best = []
    for elem in graph[next]:
        if elem not in done:
            s = backtrack(done + [next], [e for e in todo if e != next], elem)
            if len(s) > len(best):
                best = s
        else:
            if len(done + [next]) > len(best):
                best = done + [next]
    return best

graph = {}   
graph['A'] = ['B', 'D']
graph['B'] = ['C']
graph['C'] = ['A']
graph['D'] = []

print( backtrack([], ['A', 'B', 'C', 'D'], 'A') )