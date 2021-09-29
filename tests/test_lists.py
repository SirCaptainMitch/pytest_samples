import unittest
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from app.lists.list_multiplier import list_multiplier, list_multiplier_without_math
from app.lists.sum_of_array import sum_of_array
from app.lists.find_numbers import find_second_largest_number, find_smallest_number_in_list
from app.lists.generate_list_partitions import generate_list_partitions
from app.lists.split_numeric_string_to_list import split_numeric_string_to_list, parse_alphanumeric_string_for_numeric
from app.lists.rotate_array_by_chunk import rotate_array_by_chunk
from app.lists.remove_multiples import remove_multiples

class ListTest(unittest.TestCase):
  
  def test_list_multiplier(self):
    l = [1,2,3]
    expected_result = 6
    self.assertEqual(expected_result, list_multiplier(l))

  def test_list_multiplier_without_math(self):
    l = [1,2,3]
    expected_result = 6
    self.assertEqual(expected_result, list_multiplier_without_math(l))

  def test_find_second_largest_number(self):
    l = [1,2,3]
    expected_result = 2
    self.assertEqual(expected_result, find_second_largest_number(l))

  def test_find_smallest_number_in_list(self):
    l = [1,2,3]
    expected_result = 1
    self.assertEqual(expected_result, find_smallest_number_in_list(l))

  def test_generate_list_partitions(self):
    l = [1,2,3]
    expected_result = [
        [10, 20],
        [30, 40],
        [50, 60],
        [70, 80],
        [90, 100],
        [110]
      ]
    self.assertEqual(expected_result, generate_list_partitions([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110], 2))

  def test_find_second_largest_number(self):
    l = [1,2,3]
    expected_result = 2
    self.assertEqual(expected_result, find_second_largest_number(l))

  def test_sum_of_array(self):
    number = 10
    array = [*range(1,number + 1, 1)]
    expected_result = 55 
    self.assertEqual(expected_result, sum_of_array(array))

  def test_split_numeric_string_to_list(self):
    numbers = "123456789"
    expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    self.assertEqual(expected_result, split_numeric_string_to_list(numbers))

  def test_parse_alphanumeric_string_for_numeric(self):
    numbers = "12A34B567C89"
    expected_result = {
      'numeric_list': [1, 2, 3, 4, 5, 6, 7, 8, 9]
      , 'alpha_list': ['A', 'B', 'C']
    }
    self.assertEqual(expected_result, parse_alphanumeric_string_for_numeric(numbers))

  def test_rotate_array_by_chunk(self):
    arr = [x for x in range(1, 8)]
    size = len(arr)
    chunk = 2 
    expected_result = [3, 4, 5, 6, 7, 1, 2]
    self.assertEqual(expected_result, rotate_array_by_chunk(arr, size, chunk))

  def test_remove_multiples(self):
    l = [1,2,2,3,4,4,4,5]
    expected_result = [1,2,3,4,5]
    self.assertEqual(expected_result, remove_multiples(l))