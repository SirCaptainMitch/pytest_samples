""" 

  Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements. 

  This: [1, 2, 3, 4, 5, 6, 7]
  Becomes: [3, 4, 5, 6, 7, 1, 2]

"""

def rotate_array_by_chunk(arr, length, chunk):

  arr[:] = arr[chunk:length] + arr[0:chunk]

  return arr

