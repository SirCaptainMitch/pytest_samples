import unittest
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from app.basics.addition import simple_addition
from app.basics.factorial import compute_factorial, compute_factorial_prod, compute_factorial_without_math
from app.basics.max_two_numbers import find_max_two_numbers
from app.basics.simple_interest import calc_simple_interest
from app.basics.complex_interest import calc_complex_interest
from app.basics.series_cube_sum import series_cube_sum

class BasicTest(unittest.TestCase):
  
  def test_simple_addition(self):
    first = 1
    second = 2
    expected_result = first + second
    self.assertEqual(expected_result, simple_addition(first, second))

  def test_compute_factorial(self):
    number = 6 
    expected_result = 720
    self.assertEqual(expected_result, compute_factorial(number))

  def compute_factorial_prod(self):
    number = 6 
    expected_result = 720
    self.assertEqual(expected_result, compute_factorial_prod(number))

  def compute_factorial_without_math(self):
    number = 6 
    expected_result = 720
    self.assertEqual(expected_result, compute_factorial_without_math(number))

  def test_find_max_two_numbers(self):
    expected_result = 100 
    self.assertEqual(expected_result, find_max_two_numbers(1, 100))

  def test_calc_simple_interest(self):
    principle = 10000
    time = 5
    rate = 5
    expected_result = 2500
    self.assertEqual(expected_result, calc_simple_interest(principle, time, rate))

  def test_calc_complex_interest(self):
    principle = 1200
    time = 2
    rate = 5.4
    expected_result = 133.10
    self.assertEqual(expected_result, calc_complex_interest(principle, time, rate))

  def test_series_cube_sum(self):
    n = 7 
    expected_result = 784
    self.assertEqual(expected_result, series_cube_sum(n))

