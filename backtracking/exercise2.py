# In this problem we want to help two partners that want a commercial society to dissolve. The commercial
# company has n assets and each asset has associated a positive value (profit). The partners want to divide the n
# assets between the two so that each partner corresponds exactly with half of the value (profit) of the company.
# Design a backtracking algorithm that finds all possible asset distributions. Determine if there is a greedy strategy
# to find a cast. For example, consider the following assets:
def divide_assets(assets: list[int], partner1: list[int] = [], partner2: list[int]  = []):
    if not assets:
        if calc_value(partner1) == calc_value(partner2):
            return [(partner1, partner2)]
        else:
            return None
        
    sol = []
    for element in assets:

        asets_copy = assets[:]
        asets_copy.remove(element)
        sol1 = divide_assets(asets_copy, partner1 + [element], partner2)
        if sol1:
            sol.append(sol1)
        sol2 = divide_assets(asets_copy, partner1, partner2 + [element])
        if sol2:
            sol.append(sol2)
        print(sol)
    return sol


def calc_value(list: list[int]):
    sum = 0
    for element in list:
        sum+= value_list[element-1]
    return sum

def repartir( assets, solucio = [] ) -> list[list]:
   if sum(solucio) == sum(assets):
      return solucio
   
   solucions = []
   for asset in assets:
      s = repartir( [x for x in assets if x != asset], solucio + [asset] )
      solucions += s
   return solucions

asset_list = [1,2,3,4,5,6,7,8,9,10]
value_list = [10, 9, 5, 3, 3, 2, 2, 2, 2, 5]
print(repartir(asset_list))