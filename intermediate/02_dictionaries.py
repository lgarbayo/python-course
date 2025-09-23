def find_first_sum(nums, goal):
  seen = {} # diccionario para guardar el numero y su índice

  for index, value in enumerate(nums):
    missing = goal - value
    if missing in seen: return [seen[missing], index]
    seen[value] = index # guardar el número actual a los vistos, porque no hemos encontrado la combinación

  return None

nums = [4, 5, 6, 2]
goal = 8
result = find_first_sum(nums, goal) # [2, 3] 
print(result)