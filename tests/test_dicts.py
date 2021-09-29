import unittest
import sys
import os
import json

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from app.dicts.parse_dict import get_dict_keys, get_dict_keys_and_values, get_dict_key_value, load_dict_and_get_keys

class DictTest(unittest.TestCase):
  
  path = "./app/data/tstm.json"

  with open(path, 'r', encoding='utf-8') as file:
    obj = json.load(file)

  def test_get_dict_keys(self):
    expected_result = [
      'assistant_captain', 
      'captain', 
      'division_concat', 
      'division_display_name', 
      'hp_mmr_avg', 
      'ngs_id', 
      'ngs_mmr_avg', 
      'roster_path', 
      'team_description', 
      'team_members', 
      'team_mmr_avg', 
      'team_name', 
      'team_name_lower', 
      'ticker', 
      'ticker_lower']
    self.assertEqual(expected_result, get_dict_keys(self.obj))


  def test_load_dict_and_get_keys(self):
    expected_result = [
      'assistant_captain', 
      'captain', 
      'division_concat', 
      'division_display_name', 
      'hp_mmr_avg', 
      'ngs_id', 
      'ngs_mmr_avg', 
      'roster_path', 
      'team_description', 
      'team_members', 
      'team_mmr_avg', 
      'team_name', 
      'team_name_lower', 
      'ticker', 
      'ticker_lower']
    self.assertEqual(expected_result, load_dict_and_get_keys(self.path))


  def test_get_dict_key_value(self):
    key = 'ticker_lower'
    expected_result = ['Key: ticker_lower - Value: tstm ']
    self.assertEqual(expected_result, get_dict_key_value(self.obj, key))
    
