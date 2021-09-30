
def union(list):

  id_list = [y for x in list for y in x]
  output = [x for x in set(id_list)]
  output.sort()
  return output


def intersect(list):

  id_list = [y for x in list for y in x]
  output = [x for x in set(id_list) if id_list.count(x) > 1]
  output.sort()
  return output


def lookup(obj, tag_list):
  return {k:v for (k, v) in obj.items() if k in tag_list}


def query_parser(obj, query):

  operator_list = ['AND', 'OR']

  if query[0] in operator_list:
    if query[0] == 'AND':
      tag_list = query[1:]
      output = lookup(obj, tag_list)
      id_list = [x for x in [v for (k,v) in output.items()]]
      return intersect(id_list) if len(tag_list) > 1 else id_list[0]

    if query[0] == 'OR':
      tag_list = query[1:]
      output = lookup(obj, tag_list)
      id_list = [x for x in [v for (k,v) in output.items()]]
      return  union(id_list)


def query_search(obj, query):
  
  operator_list = ['AND', 'OR']

  key_list = [x for x in obj]
  tag_list = [x for x in query[1:] if x in key_list]
  sub_list = [x for x in query[1:] if x not in key_list]

  output = [ ]
  pl1 = [] 
  pl2 = []
  pl3 = []

  if query[0] not in operator_list:
    output = ( v for (k,v) in (lookup(obj, query)).items()).__next__()
    return output

  if query[0] in operator_list:
    filtered_obj = lookup(obj, tag_list)
    pl1 = query_parser(filtered_obj, [query[0]] + tag_list)

    if len(sub_list) > 0:
      for q in sub_list:       
        r_tag_list = [ x for x in q[1:] if x in key_list]
        r_sub_list = [x for x in q[1:] if x not in key_list]
        
        filtered_obj = lookup(obj, r_tag_list)        
        pl2 = pl2 + query_parser(filtered_obj, q)

        if len(r_sub_list) > 0:
          pl2 = pl2 + (query_search(obj, x) for x in r_sub_list).__next__()


  if query[0] == 'OR':
    output = union([pl1, pl2, pl3])

  if query[0] == 'AND':
    output = intersect([pl1, pl2, pl3])
    if len(output) == 0:
      output = pl1
  return output



