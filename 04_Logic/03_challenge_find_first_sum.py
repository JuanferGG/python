"""
Dado un array de números y un número goal, 
encuentra los dos primeros números del array que sumen el número goal y devuelve sus índices. 
Si no existe tal combinación, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""
nums = [4, 5, 6, 2]
goal = 8


def find_goal(list, goal):

    if len(list) == 0: return None

    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] + list[j] == goal:
                return print(f"Los indices son: {[i, j]}")


def find_first_sum(nums, goal):
  seen = {} #* diccionario para guardar el numero y su índice

  for index, value in enumerate(nums):
    missing = goal - value
    if missing in seen: return [seen[missing], index]
    seen[value] = index #* guardar el número actual a los vistos, porque no hemos encontrado la combinación

  return None


find_goal(nums, goal)