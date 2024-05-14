# Given a graph, design an algorithm to find a cycle in a graph.
def  backtracking(graph, done: list, nodes: list, node_actual):
    # si ens quedem sense nodes per on passar retornem la llista buida
    if not nodes:
        return []
    
    # Si ja em passat per auqest node estara a done i per tant es un cicle
    if node_actual in done:
        return done
    
    # Si arribem aaqui 
    solution = []
    # mirar possibles camins
    for elem in graph[node_actual]:
        # comprobar si arribem a una solucio afegint el node actual a done i treientlo dels nodes per explorar
        # també s'ha de actualitzar el node actual
        solution = backtracking(graph, done + [node_actual], [e for e in nodes if e != node_actual], elem)
        # si trobem algo parar el bucle i retornar
        if solution:
            break
    return solution

graph = {}   
graph['A'] = ['B', 'D']
graph['B'] = ['C']
graph['C'] = ['A']
graph['D'] = []


print( backtracking( graph, [], ['A', 'B', 'C', 'D'], 'A') )