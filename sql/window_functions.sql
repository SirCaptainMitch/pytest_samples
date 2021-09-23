
-- What is the count of people that were made valid per day? 
 
SELECT ROW_NUMBER() OVER ( ORDER BY COUNT(ValidFrom ) DESC ) AS rn 
	,COUNT(ValidFrom ) AS ValidFromCount
	,ValidFrom
FROM [application].people
GROUP BY ValidFrom 


SELECT o.OrderId
	  ,o.CustomerId
	  ,p.FullName 
	  ,SUM( NetSale ) as TotalNetSale
FROM Sales.Orders o 
	JOIN (  SELECT OrderId  
				   ,Quantity
				   ,UnitPrice
				   ,UnitPrice * Quantity AS NetSale
				   ,( ol.TaxRate / 100 ) AS TaxRate
				   ,(UnitPrice * Quantity) * ( ol.TaxRate / 100 ) AS TotalTaxes 
			FROM Sales.OrderLines ol
		 ) AS ol ON ol.OrderId = o.OrderId
	JOIN [Application].people p ON p.PersonId = o.SalespersonPersonId
GROUP BY  o.OrderId
	  ,o.CustomerId
	  ,p.FullName  


SELECT c.CustomerName
	   ,COUNT(o.OrderId) AS TotalOrdersByYear
	   ,YEAR(o.OrderDate) AS OrderYear
	   ,DATENAME(MONTH, o.OrderDate) AS OrderMonth
FROM sales.orders o 
	JOIN sales.customers c ON c.CustomerId = o.CustomerId
GROUP BY c.CustomerName 
		,YEAR(o.OrderDate)
	    ,DATENAME(MONTH, o.OrderDate)


