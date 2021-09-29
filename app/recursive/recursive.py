# q1 = [ 'c#' ] # [1,2,3,5, 100]
# q2 = [ 'AND' , 'python', 'pandas' ] # [ 3, 5, 8, 9 ]
# q3 = [ 'OR' , 'java', 'pandas' ] # [3, 5, 8, 9] != [3, 5, 8, 9, 10, 11, 99]
q4 = [ 'AND', ['OR', 'java', "mitchLang" ], 'c#' ] # [1, 2, 3, 5, 100]
# q5 = [ 'AND', 
#   ['OR', 
#     [ 'AND',
#       'python',
#       'pandas' 
#     ],
#     'java'], 
#   'c#' 
# ] # [1, 2, 3, 5, 8, 9, 10, 11, 100]
# q6 = [ 'AND' , [ 'OR' , 'java', 'mitchLang' ], 'python', 'pandas' ] # [3, 5, 8, 9]
# q7 = [ 'OR' , [ 'AND' , 'java', 'mitchLang' ], 'python', 'pandas' ] # [3, 5, 8, 9, 14, 17, 99]
# q8 = [ 'OR' , 'python', 'pandas' ] # [3, 5, 8, 9, 14, 17, 99]

invertedList = { 
  "c#": [1,2,3,5, 100],
  "pandas": [3, 5, 8, 9, 99],
  "python": [3, 5, 8, 9, 14, 17],
  "java": [10, 11],
  "mitchLang": [100, 101]

}

def union(invertedList, tag_list):
    one = [ x for x in tag_list if x in [y for y in invertedList]]
    questions = [ v for (k,v) in invertedList.items() if k in [y for y in one ] ]
    id_list = [y for x in questions for y in x]
    output = [x for x in set(id_list)]

    return output

def intersect(invertedList, tag_list):
    one = [ x for x in tag_list if x in [y for y in invertedList]]    
    questions = [ v for (k,v) in invertedList.items() if k in [y for y in one ] ]

    if len(questions) > 1: 
      id_list = [y for x in questions for y in x]
      output = [x for x in set(id_list) if id_list.count(x) > 1]
    else: 
      output = id_list = [y for x in questions for y in x]

    return output

def recursive_query_search(obj, query):
  result = []

  l = [ k for (k,v) in obj.items() if k in [x for x in query[1:] ] ]
  sub = [x for x in query[1:] if x not in [x for x in obj]]
  
  if query[0] == 'AND': 
    result = result + intersect(obj, l)

  if len(l[1:]) > 1 :
    result = result + [ v for (k,v) in obj.items() if k == query[0] ]

  if len(l) == 0 :
    result = result + [ v for (k,v) in obj.items() if k == query[0] ][0]

  elif query[0] == 'OR':
    u = union(obj, l)
    i = intersect(obj, u + result) 
    if len(i) > 0:
      result = result + i 
    else:
      result = result + u      

  if len(sub) > 0:
    for q in sub:
      r = recursive_query_search(obj, q)
      i = intersect(obj, r + result)
      if len(i) > 0:
        result = result + r 
      else:
        result = result + i

  result = [x for x in set(result)]
  result.sort()
  return result

print(recursive_query_search(invertedList, q4))
# print(recursive_query_search(invertedList, q1))

