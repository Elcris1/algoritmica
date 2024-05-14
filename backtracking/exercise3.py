# Consider n different letters. Design a backtracking algorithm that finds all words of length m, with m < n,
# without letter repetition.
def find_combinations(alphabet: list[str], length: int, sol = []):
    if len(sol) == length:
        return [sol]
    
    solution = []
    for x in alphabet:
        # OPCION 1:
        if x not in sol:
            s = find_combinations(alphabet, length, sol + [x])
            solution += s

        # OPCION 2:
        # cop = alphabet[:]
        # cop.remove(x)
        
        # s = find_combinations(cop, length, sol + [x])
        # solution += s
        
    return solution
n = ["A", "B", "C", "D"]
m = 3

print(find_combinations(n, m))