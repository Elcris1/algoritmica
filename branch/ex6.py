"""
Given a set of items with different sizes and a fixed number of bins, find the minimum number of bins required to
pack all items, subject to the constraint that the total size of items in each bin does not exceed a given capacity.
"""

def branchandbound(todo, done, best, tope_basures, capacity_basures):
    if not todo:
        return len(done)
    if lb(todo, done, capacity_basures) >= best:
        return best
    
    for element in todo:
        esta = False
        for basura in done:
            if done[basura] - element >= 0:
                done[basura] -= element
                s = branchandbound([x for x in todo if x != element], done, best, tope_basures, capacity_basures)
                esta = True
                break

        print(not esta and len(done) < tope_basures)
        if not esta and len(done) < tope_basures:
            done[len(done) + 1] = capacity_basures - element

        if len(done) < best:
            best = len(done)
        
    return best

def lb(todo, done, capacity_basures):
   return sum(todo) / capacity_basures + len(done)
            
print(branchandbound([1,2,3,4,5], {0: 10}, 100, 5, 5))