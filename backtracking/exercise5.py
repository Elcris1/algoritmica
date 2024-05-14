# Consider a board of n × n positions and a set of n colors. A latin square n × n s is a board such that the same
# color is not repeated either in a row or in a column. Design a backtracking algorithm that shows all the latin
# squares of n × n that can be obtained with n different colors.

def backtrack(matriz, n: list[str], sol = []):
    pos = isEmpty(matriz)
    if not pos:
        #solutions.append(matriz) no va porque si modificamos matriz mas alante peta
        # se teine que añadir de la siguiente forma
        sol.append([row[:] for row in matriz])
        return
        # esto retornaba False
    
    for elem in n:
        if valid_pos(matriz, elem, pos[0], pos[1]):
            matriz[pos[0]][pos[1]] = elem

            # Opcion 1
            backtrack(matriz, n, sol)

            matriz[pos[0]][pos[1]] = ""

            # codigo hecho por mi con unICA SOLUCION OPCION 2
            # if backtrack(matriz, n):
            #     return True
                
    #return Falase        


def valid_pos(matriz: list[list[str]], elem: str, row: int, col: int):
    # comprovar fila
    if elem in matriz[row]:
        return False
    
    # Comprovar columna
    for r in range(len(n)):
        if elem == matriz[r][col]:
            return False
        
    return True

def isEmpty(matriz):
    l = len(matriz)
    for r_el in range(l):
        for c_el in range(l):
            if matriz[r_el][c_el] == "":
                return (r_el, c_el)
    return False   
n = ["RED", "GREEN", "BLUE"]
board = [[0, 1, 2],
         [3, 4, 5],
         [6, 7, 8]]

matriz = [["" for _ in range(len(n))] for _ in range(len(n))]
solutions = []
backtrack(matriz, n, solutions)
for elem in solutions:
    print(elem)
