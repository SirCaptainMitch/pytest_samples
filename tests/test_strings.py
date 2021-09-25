import unittest
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from app.strings.find_substring import string_exists_with_index
from app.strings.find_substring import string_exists_regex
from app.strings.find_substring import string_exists_contains
from app.strings.find_substring import find_string

class StringTest(unittest.TestCase):
  
  def test_string_exists_with_index(self):
    string = 'The quick Brown fox jumped over the lazy dog'
    search_string = 'quick brown'
    expected_result = True
    self.assertEqual(expected_result, string_exists_with_index(search_string, string))

  def test_string_exists_regex(self):
    string = 'The quick Brown fox jumped over the lazy dog'
    search_string = 'quick brown'
    expected_result = True
    self.assertEqual(expected_result, string_exists_regex(search_string, string))

  def test_string_exists_contains(self):
    string = 'The quick Brown fox jumped over the lazy dog'
    search_string = 'quick brown'
    expected_result = False
    self.assertEqual(expected_result, string_exists_contains(search_string, string))

  def test_find_string(self):
    string = 'The quick Brown fox jumped over the lazy dog'
    search_string = 'quick brown'
    expected_result = 'quick brown'
    self.assertEqual(expected_result, find_string(search_string, string))
