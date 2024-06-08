# In this problem we want to help two partners that want a commercial society to dissolve. The commercial
# company has n assets and each asset has associated a positive value (profit). The partners want to divide the n
# assets between the two so that each partner corresponds exactly with half of the value (profit) of the company.
# Design a backtracking algorithm that finds all possible asset distributions. Determine if there is a greedy strategy
# to find a cast. For example, consider the following assets:
def backtracking(todo, partner1 = [], partner2 = []):
    if not todo:
        if count(partner1) == count(partner2):
            return [(partner1, partner2)]
        else:
            return None
    
    sol = []
    for element in todo:
        s1 = backtracking([x for x in todo if x != element], partner1 + [element], partner2)
        if s1:
            sol.append(s1)

        s2 = backtracking([x for x in todo if x != element], partner1, partner2 + [element])
        if s2:
            sol.append(s2)
    return sol
def count(current):
    sum = 0
    for element in current:
        sum += value_list[element-1]
    return sum  

asset_list = [1,2,3,4,5,6,7,8,9,10]
value_list = [10, 9, 5, 3, 3, 2, 2, 2, 2, 4]


print(backtracking(asset_list))