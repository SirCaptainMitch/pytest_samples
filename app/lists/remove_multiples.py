def remove_multiples(list): 

  result = [x for x in set(list)]

  return result

print(remove_multiples([1,2,2,3,4,4,4,5]))