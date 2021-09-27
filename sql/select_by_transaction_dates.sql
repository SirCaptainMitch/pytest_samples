-- FIRST / LAST 
SELECT DISTINCT ct.CustomerId
	  ,FIRST_VALUE(ct.TransactionDate) OVER ( ORDER BY ct.CustomerId ) FirstTransaction
	  ,LAST_VALUE(ct.TransactionDate) OVER ( ORDER BY ct.CustomerId ) LastTransaction
FROM sales.CustomerTransactions ct
WHERE 1=1 
	-- AND ct.CustomerId = 925

-- MIN / MAX 

SELECT DISTINCT ct.CustomerId
	  ,MAX(ct.TransactionDate) OVER ( PARTITION BY ct.CustomerId ) FirstTransaction
	  ,MIN(ct.TransactionDate) OVER ( PARTITION BY ct.CustomerId ) LastTransaction
FROM sales.CustomerTransactions ct
WHERE 1=1 
	-- AND ct.CustomerId = 925

-- ROW_NUMBER() to get Second Transaction by Customer
SELECT * 
FROM ( 
		SELECT ROW_NUMBER() OVER  (PARTITION BY CustomerId ORDER BY ct.TransactionDate ASC) AS rn
			  ,ct.CustomerId
			  ,ct.TransactionDate AS SecondTransactionDate
		FROM sales.CustomerTransactions ct
		WHERE 1=1 
		 --AND ct.CustomerId = 1
) AS sub 
WHERe sub.rn = 2