#Com que els generals no estan mai contents, ara resulta que no els agrada el dest´ ı que Hann´ ıbal els ha triat. Cada general ha fet una llista de destins als que li agradaria anar. Cada general ha d’anar a un dest´ ı, i nom` es a un. Si ´es possible trobar-ho, podrieu adjudicar a cada general un dest´ ı de forma que el resultat agradi a tots els generals?
def backtracking(todo, preferencies, general = 0, done = [] ):
    if not todo:
        return done
    
    sol = []
    for destinacio in todo:
        if destinacio in preferencies[general] and destinacio not in done:
            s = backtracking([x for x in todo if x != destinacio], preferencies, general+1, done + [destinacio])
            if s:
                sol.append(s)
    return sol


destinacions = ["S", "Y", "U", "N", "L", "C"]
generals = [1, 2, 3, 4, 5, 6]
preferencies = [["S", "C"], ["S", "Y"], ["C", "U", "Y"], ["N", "C", "L"], ["Y", "L"], ["S", "N", "C", "Y"]]

print(backtracking(destinacions, preferencies))