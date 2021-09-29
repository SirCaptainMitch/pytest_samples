import math 

def list_multiplier(list):

  return math.prod(list)


def list_multiplier_without_math(list):

  total = 1

  for x in list: 
    total = x * total 

  return total
