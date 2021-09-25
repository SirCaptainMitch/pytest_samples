from math import factorial, prod

# factorial = multiplication of all positive integers that are >= $number 
# ( e.g. 6! = 6*5*3*4*2*1 = 720)

def compute_factorial(number):  
  return(factorial(number))


def compute_factorial_prod(number):
  number_list = [*reversed(range(1, number + 1, 1 ))]
  return prod(number_list)


def compute_factorial_without_math(number):
  number_list = [*reversed(range(1, number + 1, 1 ))]
  total_sum = 1
  for x in number_list:
    total_sum = total_sum * x  
  return total_sum

