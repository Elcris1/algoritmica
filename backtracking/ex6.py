# Given a graph, design an algorithm to find a cycle in a graph.
def backtracking(todo, done, node_actual, graph):
    if not todo or graph[node_actual] == []:
        return None
    if node_actual in done:
        return done
    sol = []
    for node in graph[node_actual]:
        s = backtracking([x for x in todo if x != node_actual], done + [node_actual], node, graph)
        if s:
            return s
    return sol


graph = {}   
graph['A'] = ['B', 'D']
graph['B'] = ['C']
graph['C'] = ['A']
graph['D'] = []

print(backtracking(['A', 'B', 'C', 'D'], [], 'A', graph))