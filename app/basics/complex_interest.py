import math 
"""
Formula to calculate compound interest annually is given by: 
A = P(1 + R/100) t 
Compound Interest = A – P 
Where, 
A is amount 
P is principle amount 
R is the rate and 
T is the time span
""" 

def calc_complex_interest(principle, timespan, rate): 
    
  amount = principle * math.pow(( 1 + rate / 100 ), timespan)
  compound_interest = round(amount - principle,1)

  return compound_interest

