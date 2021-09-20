import unittest
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from app.basics.addition import simple_addition
from app.basics.factorial import compute_factorial
from app.basics.max_two_numbers import find_max_two_numbers
from app.basics.simple_interest import calc_simple_interest

class BasicTest(unittest.TestCase):
  
  def test_simple_addition(self):
    first = 1
    second = 2
    expected_result = first + second
    self.assertEqual(expected_result, simple_addition(first, second))

  def test_compute_factorial(self):
    expected_result = 720
    self.assertEqual(expected_result, compute_factorial(6))

  def test_find_max_two_numbers(self):
    expected_result = 100 
    self.assertEqual(expected_result, find_max_two_numbers(1, 100))

  def test_calc_simple_interest(self):
    principle = 10000
    time = 5
    rate = 5
    expected_result = 2500
    self.assertEqual(expected_result, calc_simple_interest(principle, time, rate))

