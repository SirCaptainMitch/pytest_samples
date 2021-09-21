import unittest
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from app.lists.list_multplier import list_multplier
from app.lists.find_second_largest_number import find_second_largest_number

class ListTest(unittest.TestCase):
  
  def test_list_multplier(self):
    l = [1,2,3]
    expected_result = 6
    self.assertEqual(expected_result, list_multplier(l))

  def test_find_second_largest_number(self):
    l = [1,2,3]
    expected_result = 2
    self.assertEqual(expected_result, find_second_largest_number(l))

