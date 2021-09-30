q1 = [ 'c#' ] # [1,2,3,5,100]
q2 = [ 'AND' , 'python', 'pandas', 'c#' ] # [ 3, 5, 8, 9 ]
q3 = [ 'OR' , 'java', 'pandas', 'python' ] # [3, 5, 8, 9, 10, 11, 14, 17, 99]
q4 = [ 'AND', ['OR', 'java', "mitchLang" ], 'c#' ] # [100]
q5 = [ 'AND', 
  ['OR', 
    [ 'AND',
      'python',
      'pandas' 
    ],
    'java'], 
  'c#' 
] # [3,5]
q6 = [ 'OR', 
  ['OR', 
    [ 'AND',
      'python',
      'pandas' 
    ],
    'java'], 
  'c#' 
] # [1, 2, 3, 5, 8, 9, 10, 11, 100]

q7 = [ 'OR', 
  ['AND', 
    [ 'AND',
      'python',
      'pandas' 
    ],
    'java'], 
  'c#' 
] # [1, 2, 3, 5, 8, 9, 100]


data = { 
  "c#": [1,2,3,5, 100],
  "pandas": [3, 5, 8, 9, 99],
  "python": [3, 5, 8, 9, 14, 17],
  "java": [10, 11],
  "mitchLang": [100, 101]
}