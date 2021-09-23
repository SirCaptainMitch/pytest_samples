-- EXCEPT -- ROWS that are in FirstTable that are NOT in SecondTable
SELECT TOP ( 10 ) 
	ROW_NUMBER() OVER (ORDER BY FirstTable.Object_Id ) AS n
FROM sys.all_columns  FirstTable
EXCEPT
SELECT TOP ( 11 ) 
	ROW_NUMBER() OVER (ORDER BY SecondTable.Object_Id ) AS n
FROM sys.all_columns  SecondTable  


-- EXCEPT -- ROWS that are in FirstTable that are NOT in SecondTable 
SELECT TOP ( 11 ) 
	ROW_NUMBER() OVER (ORDER BY FirstTable.Object_Id ) AS n
FROM sys.all_columns  FirstTable
EXCEPT
SELECT TOP ( 10 ) 
	ROW_NUMBER() OVER (ORDER BY SecondTable.Object_Id ) AS n
FROM sys.all_columns  SecondTable 


-- INTERSECT -- ROWS that are in BOTH FirstTable and SecondTable 
SELECT TOP ( 11 ) 
	ROW_NUMBER() OVER (ORDER BY FirstTable.Object_Id ) AS n
FROM sys.all_columns  FirstTable
INTERSECT
SELECT TOP ( 10 ) 
	ROW_NUMBER() OVER (ORDER BY SecondTable.Object_Id ) AS n
FROM sys.all_columns  SecondTable 

