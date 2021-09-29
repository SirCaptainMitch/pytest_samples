
def split_numeric_string_to_list(numbers):

  try: 
    
    list = [int(x) for x in numbers if str(numbers).isnumeric()]

  except:
    return "parameter is not numeric"

  return list


def parse_alphanumeric_string_for_numeric(numbers):

  try: 

    return { 
      'numeric_list': [int(x) for x in numbers if str(x).isnumeric()], 
      'alpha_list': [x for x in numbers if str(x).isalpha()]
    }

  except:
    
    return "invalid parameter {0}".format(numbers)
