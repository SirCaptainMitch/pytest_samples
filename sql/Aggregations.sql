DECLARE @FullName VARCHAR(255) = 'Kayla Woodcock'

-- Bucketing / Quartiles using NTILE 

SELECT SUBSTRING(p.FullName, 0, CHARINDEX(SPACE(1), p.FullName) ) AS FirstName 
	  ,SUBSTRING(p.FullName, CHARINDEX(SPACE(1), p.FullName), LEN(p.FullName)) AS LastName
	  ,NTILE(4) OVER(PARTITION BY YEAR(o.OrderDate) ORDER BY YEAR(o.OrderDate) DESC, SUM(NetSale) DESC) AS Quartile  
	  ,CONVERT(NVARCHAR(20), SUM( NetSale ),1) AS SalesYTD
	  --,SUM( ol.TotalUnitPrice + TotalTaxes ) as TotalCustomerOrderCost
	  ,YEAR(o.OrderDate) AS SalesYear
FROM [application].people AS p
	JOIN Sales.Orders o ON o.SalesPersonPersonId = p.PersonId
	JOIN (  SELECT OrderId  
				   ,Quantity
				   ,UnitPrice
				   ,UnitPrice * Quantity AS NetSale
				   ,( ol.TaxRate / 100 ) AS TaxRate
				   ,(UnitPrice * Quantity) * ( ol.TaxRate / 100 ) AS TotalTaxes 
			FROM Sales.OrderLines ol
		 ) AS ol ON ol.OrderId = o.OrderId
WHERE 1=1 
	 --AND p.FullName = @FullName 
	 --AND o.OrderDate >= DATEADD(YEAR, -20, GETDATE())
GROUP BY p.FullName
		 ,YEAR(o.OrderDate)
ORDER BY YEAR(o.OrderDate) DESC 


-- Percentile Ranking based on net sales per year 

SELECT SUBSTRING(p.FullName, 0, CHARINDEX(SPACE(1), p.FullName) ) AS FirstName 
	  ,SUBSTRING(p.FullName, CHARINDEX(SPACE(1), p.FullName), LEN(p.FullName)) AS LastName
	  ,ROUND(PERCENT_RANK() OVER(PARTITION BY YEAR(o.OrderDate) ORDER BY YEAR(o.OrderDate) DESC, SUM(NetSale) DESC), 2) AS Quartile
	  ,CONVERT(NVARCHAR(20), SUM( NetSale ),1) AS SalesYTD
	  --,SUM( ol.TotalUnitPrice + TotalTaxes ) as TotalCustomerOrderCost
	  ,YEAR(o.OrderDate) AS SalesYear
FROM [application].people AS p
	JOIN Sales.Orders o ON o.SalesPersonPersonId = p.PersonId
	JOIN (  SELECT OrderId  
				   ,Quantity
				   ,UnitPrice
				   ,UnitPrice * Quantity AS NetSale
				   ,( ol.TaxRate / 100 ) AS TaxRate
				   ,(UnitPrice * Quantity) * ( ol.TaxRate / 100 ) AS TotalTaxes 
			FROM Sales.OrderLines ol
		 ) AS ol ON ol.OrderId = o.OrderId
WHERE 1=1 
	 --AND p.FullName = @FullName 
	 --AND o.OrderDate >= DATEADD(YEAR, -20, GETDATE())
GROUP BY p.FullName
		 ,YEAR(o.OrderDate)
ORDER BY YEAR(o.OrderDate) DESC

/* 

Simple Interest = (P x T x R)/100
Where,
P is the principle amount
T is the time and
R is the rate

*/ 

DECLARE @PrincipleAmount DECIMAL(8,2) = 10000 
	    ,@TimeInMonths INT = 5
		,@InterestRate DECIMAL(4, 2) = 5 

SELECT @PrincipleAmount * @TimeInMonths * @InterestRate / 100

SELECT  @PrincipleAmount  = 5600.00
	    ,@TimeInMonths = 5
		,@InterestRate  = 15.00

SELECT @PrincipleAmount * @TimeInMonths * @InterestRate / 100

-- Using this to .just show an example of what it might look like. Using Tax Rate as Interest Rate. 
 SELECT OrderId  
		,Quantity
		,UnitPrice
		,UnitPrice * Quantity AS NetSale
		,( ol.TaxRate / 100 )  AS InterestRate 
		,( ( UnitPrice * Quantity ) * @TimeInMonths * ol.TaxRate ) / 100  AS NetTotalInterestPaid
		,( ( ( UnitPrice * Quantity ) * @TimeInMonths * ol.TaxRate ) / 100 )  + ( UnitPrice * Quantity ) AS NetLifetimeTotalPaid
FROM Sales.OrderLines ol