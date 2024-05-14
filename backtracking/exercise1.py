# Let A be a set of n different integers (positive and negative). Given two integers m and C, being m < n, design
# an backtracking algorithm that finds all the subsets of A composed exactly for m items and such that the sum
# of the values of these m elements is C.
def sumValue( todo: list[int], value, length, done = []):
 
    if len(done) == length and sum(done) == value :
        return done
    
    if sum(done) > value or len(done) > length:
        return None

    solution = []
    for element in todo:
        if element not in done:
            s = sumValue(todo, value, length, done+[element])
            if s:
                solution.append(s)


    return solution


arr = [1,2,3,4,5]
n = len(arr)
m = 3
c = 8

print(sumValue(arr, c, m))
