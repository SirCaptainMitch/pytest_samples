"""
break list into chunks based on paramter. 

List comprehenstion probably best for this, handles odd / even numbered lists. 

list[x:x + chunk_size] - select values from list based on range of X + the chunk size. 
for x in range(0, len(list), chunk_size) - create the range, with an increment = to the chunk size
  to determine the number of iterations required. 

"""


def generate_list_partitions(list, chunk_size):
  
  list_of_lists = [ list[x:x + chunk_size] for x in range(0, len(list), chunk_size) ]
  
  return list_of_lists 
