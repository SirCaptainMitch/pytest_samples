import unittest
import sys
import os
from tests.queries import q1, q2, q3, q4, q5, q6, q7, data

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from app.recursive.recursive import query_search

class RecursiveTest(unittest.TestCase):  

  def test_query_search_simple(self):
    expected_result = [1,2,3,5,100]
    self.assertEqual(expected_result, query_search(data, q1))

  def test_query_search_simple_and(self):
    expected_result = [ 3, 5, 8, 9 ]
    self.assertEqual(expected_result, query_search(data, q2))

  def test_query_search_simple_or(self):
    expected_result = [3, 5, 8, 9, 10, 11, 14, 17, 99]
    self.assertEqual(expected_result, query_search(data, q3))
    
  def test_query_search_simple_nested(self):
    expected_result = [100]
    self.assertEqual(expected_result, query_search(data, q4))

  def test_query_search_complex_nested_and_or_and(self):
    expected_result = [3,5]
    self.assertEqual(expected_result, query_search(data, q5))

  def test_query_search_complex_nested_or_or_and(self):
    expected_result = [1, 2, 3, 5, 8, 9, 10, 11, 100]
    self.assertEqual(expected_result, query_search(data, q6))

  def test_query_search_complex_nested_and(self):
    expected_result = [1, 2, 3, 5, 8, 9, 100]
    self.assertEqual(expected_result, query_search(data, q7))

