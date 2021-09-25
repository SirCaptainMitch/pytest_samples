import re

def string_exists_with_index(search_string, string):
		"""
						convert the strings to lower, then search 
		"""
		string = str(string).lower()
		search_string = str(search_string).lower()

		start = string.find(search_string)
		end = start + len(search_string)
		return True if string[start:end] else False


def string_exists_regex(search_string, string):
		"""
						regex search for string, case insensitive
		"""
		string = str(string).lower()
		search_string = str(search_string).lower()
		pattern = '({s})'.format(s=search_string)
		compiled = re.compile(pattern)
		result = (re.search(compiled, string))
		return True if result else False


def string_exists_contains(search_string, string):
		"""
						basic contains logic, case sensitive
		"""
		return True if search_string in string else False


def find_string(search_string, string):
		"""
						regex search for string, case insensitive
						returns sting if found.
						else returns 'not found'
		"""
		string = str(string).lower()
		search_string = str(search_string).lower()
		pattern = '({s})'.format(s=search_string)
		compiled = re.compile(pattern)
		result = (re.search(compiled, string))
		return result[0] if result else 'Not found'
