DECLARE @ListToPivot NVARCHAR(255) = ( 
										SELECT STRING_AGG( OrderDate , ', ') WITHIN GROUP (ORDER BY OrderDate DESC)
										FROM ( SELECT DISTINCT CONCAT('[', YEAR(OrderDate), ']') AS OrderDate 
											   FROM Sales.Orders o 
											 ) AS o
									  )
	,@SQL NVARCHAR(MAX) 
	,@PivotColumn NVARCHAR(MAX) = 'SalesYear'
	,@Aggregate NVARCHAR(MAX) = 'SUM(SalesYTD)'
	,@TableName NVARCHAR(MAX) = 'CustomerSalesByYear'
	,@SqlStatement NVARCHAR(MAX)

SELECT @SQL = '
		SELECT *
		FROM  ( 
				SELECT  DISTINCT c.CustomerName
						,SUM(ol.UnitPrice * ol.Quantity) OVER ( PARTITION BY c.CustomerName, YEAR(o.OrderDate) ORDER BY YEAR(o.OrderDate) ) AS SalesYTD
						,YEAR(o.OrderDate) AS SalesYear
				FROM Sales.Orders o
						JOIN Sales.Customers c ON c.CustomerId = o.CustomerId
						--JOIN [Application].People p ON p.PersonId = o.SalesPersonPersonId
						JOIN Sales.OrderLines ol ON ol.OrderId = o.OrderId
				WHERE 1=1
		) AS sub
		WHERE 1=1
' 

SET NOCOUNT ON
SET @SqlStatement = N'
DROP TABLE IF EXISTS dbo.' + @TableName + '
SELECT * 
INTO dbo.' + @TableName + '
FROM ( ' + 
	@SQL 
+ '
) map
PIVOT (
	' + @Aggregate + '
	FOR ' + @PivotColumn + '
		IN (
		'+@ListToPivot+'
		)
) AS PivotTable

SELECT * 
FROM dbo.CustomerSalesByYear
WHERE 1=1 ' + 
	--' AND CustomerName = ' + QUOTENAME('Aakriti Byrraju', '''') + CHAR(10) +
'ORDER BY CustomerName DESC'
;
PRINT @SqlStatement
EXEC(@SqlStatement)

