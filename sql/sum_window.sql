-- SUM total sales / quantity by item, sales person, customer. 
SELECT c.CustomerName
	  ,p.FullName AS SalesPerson
	  ,SUM(ol.UnitPrice * Quantity) AS NetSale
FROM Sales.Orders o
	 JOIN Sales.Customers c ON c.CustomerId = o.CustomerId
	 JOIN [Application].People p ON p.PersonId = o.SalesPersonPersonId
	 JOIN Sales.OrderLines ol ON ol.OrderId = o.OrderId
WHERE 1=1 
GROUP BY c.CustomerName
	  ,p.FullName 


-- Same song, almost the same verse. Using windowing instead of group by 
SELECT DISTINCT
	   c.CustomerName
	  ,p.FullName AS SalesPerson
	  ,SUM(ol.UnitPrice * Quantity) OVER ( PARTITION BY  c.CustomerName
														,p.FullName 
										 ) AS SalesYTD
FROM Sales.Orders o
	 JOIN Sales.Customers c ON c.CustomerId = o.CustomerId
	 JOIN [Application].People p ON p.PersonId = o.SalesPersonPersonId
	 JOIN Sales.OrderLines ol ON ol.OrderId = o.OrderId
WHERE 1=1 

