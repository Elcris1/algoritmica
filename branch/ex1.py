"""
A given multiset S of positive integers can be partitioned into two subsets S1 and S2. Partition the multiset S
into two subsets S1, S2 such that the difference between the sum of the values of the elements in S1 and the sum
of the values of the elements in S2 is minimized
""" 

def branch_bound(todo, best, list1 = [], list2 = []):
    if not todo:
        return (list1, list2)
    if lb(todo, list1, list2) >= diff(best):
        return best

    for element in todo:
        s1 = branch_bound([x for x in todo if x != element], best, list1 + [element], list2)
        if s1:
            best = min_diff(s1, best)
        s2 = branch_bound([x for x in todo if x != element], best, list1, list2 + [element])
        if s2:
            best = min_diff(s2, best)
    return best

def min_diff(t1,t2):
    if diff(t1) < diff(t2):
        return t1
    else:
        return t2

def diff(tuple):
    return abs(sum(tuple[0]) - sum(tuple[1]))

def lb(assets, sol1, sol2):
    # Cálculo de las sumas actuales de sol1 y sol2
    sum1 = sum(sol1)
    sum2 = sum(sol2)

    #Cálculo de la diferencia actual entre sol1 y sol2
    current_diff = abs(sum1 - sum2)

    #Suma de todos los activos restantes
    remaining_sum = sum(assets)

    #La cota inferior es la diferencia actual menos el máximo posible que se puede equilibrar con los activos restantes
    return current_diff - remaining_sum

print(branch_bound([1,2,3,4,5,6], ([1,2,3,4,5,6], [])))