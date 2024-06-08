# Let A be a set of n different integers (positive and negative). Given two integers m and C, being m < n, design
# an backtracking algorithm that finds all the subsets of A composed exactly for m items and such that the sum
# of the values of these m elements is C.
def backtracking(todo, done ,  m, c):
    if len(done) == m and count(done) == c:
        return done
    
    if len(done)>m or count(done) > c:
        return None
    
    sol = []
    for element in todo:
        s = backtracking([x for x in todo if x != element], done+[element], m, c )
        if s:
            sol.append(s)

    return sol

    
def count(current):
    sum = 0
    for element in current:
        sum += element
    return sum   

arr = [1,2,3,4,5]
n = len(arr)
m = 3
c = 8

print(backtracking(arr, [], m, c))