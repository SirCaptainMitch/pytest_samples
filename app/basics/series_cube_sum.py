import math 

""" 
for a given postive number ( n ), find the sum of all cubed integers that are <= n ) 
"""

def series_cube_sum( number ):
  integer_list = [*range(1, number + 1, 1)]
  total_sum = sum([*map(lambda x: math.pow(x, 3), integer_list)])
  return total_sum
