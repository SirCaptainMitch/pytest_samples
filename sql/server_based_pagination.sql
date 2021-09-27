
-- Pagination - First 100 
DECLARE @Offset INT = 0
	   ,@Fetch INT = 100

SELECT DENSE_RANK() OVER (ORDER BY CustomerId) AS rn
	  ,ct.CustomerId
	  ,ct.TransactionDate AS SecondTransactionDate
FROM sales.CustomerTransactions ct
WHERE 1=1 
 AND ct.CustomerId = 925
ORDER BY ct.TransactionDate ASC
OFFSET @Offset ROWS 
FETCH NEXT @Fetch ROWS ONLY


-- Pagination - Second 100 
SELECT @Offset = 100
	  ,@Fetch = 100

SELECT DENSE_RANK() OVER (ORDER BY CustomerId) AS rn
	  ,ct.CustomerId
	  ,ct.TransactionDate AS SecondTransactionDate
FROM sales.CustomerTransactions ct
WHERE 1=1 
 AND ct.CustomerId = 925
ORDER BY ct.TransactionDate ASC
OFFSET @Offset ROWS 
FETCH NEXT @Fetch ROWS ONLY


