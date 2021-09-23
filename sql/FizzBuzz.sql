-- FIZZ BUZZ, because everyone wants this eventually 

DECLARE @Start INT = 1
	    ,@End INT = 10
		,@BasicEven INT = 2

DECLARE @Mod1 INT = 5 
	    ,@Mod2 INT = 3 
		,@Mod3 INT 

SET @Mod3 = ( @Mod1 + @Mod2 )

-- Basic Even / Odd
;WITH cte AS ( 
		SELECT @Start AS n
		UNION ALL 
		SELECT @Start + n 
		FROM cte 
		WHERE n + 1 <= @End
) 
SELECT CASE WHEN cte.n % @BasicEven = 0 
			THEN 'FIZZ' 
			ELSE 'BUZZ' 
			END AS FizzBuzz
FROM cte

-- Classic version 

;WITH cte AS ( 
		SELECT @Start AS n
		UNION ALL 
		SELECT @Start + n 
		FROM cte 
		WHERE n + 1 <= @End
) 
SELECT CASE WHEN cte.n % @Mod3 = 0 
			THEN 'FIZZBUZZ' 
			WHEN cte.n % @Mod1 = 0 
			THEN 'FIZZ' 
			WHEN cte.n % @Mod2 = 0 
			THEN 'BUZZ'
			ELSE CONVERT(VARCHAR(255), cte.n) 
			END AS FizzBuzz
FROM cte


-- Classic with Numbers table ( I will be using a system table instead to recreate that concept ) 

DROP TABLE IF EXISTS #MyNumbersTable

SELECT TOP ( @End ) 
	   ROW_NUMBER() OVER (ORDER BY ac.Object_Id ) AS n
INTO #MyNumbersTable
FROM sys.all_columns  ac 

SELECT CASE WHEN mnt.n % @Mod3 = 0 
			THEN 'FIZZBUZZ' 
			WHEN mnt.n % @Mod1 = 0 
			THEN 'FIZZ' 
			WHEN mnt.n % @Mod2 = 0 
			THEN 'BUZZ'
			ELSE CONVERT(VARCHAR(255), mnt.n) 
			END AS FizzBuzz
FROM #MyNumbersTable mnt

-- Second verse, mostly same as the first. 

SELECT CASE WHEN mnt.n % @Mod3 = 0 
			THEN 'FIZZBUZZ' 
			WHEN mnt.n % @Mod1 = 0 
			THEN 'FIZZ' 
			WHEN mnt.n % @Mod2 = 0 
			THEN 'BUZZ'
			ELSE CONVERT(VARCHAR(255), mnt.n) 
			END AS FizzBuzz
FROM ( 
	SELECT TOP ( @End ) 
	   ROW_NUMBER() OVER (ORDER BY ac.Object_Id ) AS n
	FROM sys.all_columns  ac 
) mnt
