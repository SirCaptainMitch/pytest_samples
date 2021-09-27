-- Dynamic SQL based Advanced Search ( this is not a good idea, but fun to write )

SET NOCOUNT ON; 
SET STATISTICS IO OFF;
SET STATISTICS TIME OFF;


-- Params 
DECLARE  @Params NVARCHAR(MAX) = '@OrderId = NULL, @CustomerId = 925' 
		,@Offset INT = 0
		,@Fetch INT = 1000
		,@RetentionDate DATETIME2 = DATEADD(YEAR, -7, GETDATE()) 

DROP TABLE IF EXISTS #Columns 


SELECT * 
INTO #Columns
FROM ( 
	SELECT RTRIM(LTRIM(c.[Value])) AS ParameterString
		   ,RTRIM(LTRIM(SUBSTRING(c.[Value], 0 , CHARINDEX('=', c.[Value])))) AS ParameterName
		   ,RTRIM(LTRIM(REPLACE(SUBSTRING(c.[Value], CHARINDEX('=', c.[Value]), LEN(c.[Value])), '=', ''))) AS ParameterValue
	FROM STRING_SPLIT(@Params, ',' ) c
	) sub 
WHERE sub.ParameterValue <> 'NULL'

--SELECT *
--FROM #Columns c

-- Config 
DECLARE  @WhereSQL NVARCHAR(MAX) = CONCAT('WHERE 1=1'
										 ,CHAR(10)
										 ,CHAR(9) 
										 ,'AND OrderDate BETWEEN '
										 ,QUOTENAME(CONVERT(NVARCHAR(50), @RetentionDate, 101), '''') 
										 ,' AND '
										 ,QUOTENAME(CONVERT(NVARCHAR(50), GETDATE(), 101), '''') 
									) 
	
		,@ColumnsSQL NVARCHAR(MAX)
		,@FromSQL NVARCHAR(MAX) = 'FROM Sales.Orders o'
		,@JoinSQL NVARCHAR(MAX)
		,@CustomerSQL NVARCHAR(MAX) = 'JOIN Sales.Customers c ON c.CustomerId = o.CustomerId'
		,@SalesPersonSQL NVARCHAR(MAX) = 'JOIN [Application].People salesPerson ON salesPerson.PersonId = o.SalesPersonPersonId '
		,@ContactPersonSQL NVARCHAR(MAX) = 'JOIN [Application].People contactPerson ON contactPerson.PersonId = o.ContactPersonId'
		,@PickedBySQL NVARCHAR(MAX) = 'JOIN [Application].People pickedByPerson ON pickedByPerson.PersonId = o.PickedByPersonId '
		,@EditedBySQL NVARCHAR(MAX) = 'JOIN [Application].People lastEditedBy ON lastEditedBy.PersonId = o.lastEditedBy'
		,@MainSQL NVARCHAR(MAX)


SET @ColumnsSQL = ' 
SELECT   o.OrderId
		,c.CustomerName
		,o.OrderDate
		,o.ExpectedDeliveryDate
		,o.CustomerPurchaseOrderNumber
		--,CustomerPrimaryContact.FullName AS CustomerPrimaryContact
		--,CustomerPrimaryContact.PhoneNumber AS CustomerPrimaryContactPhone
		--,CustomerPrimaryContact.EmailAddress AS CustomerPrimaryContactEmail
		--,CustomerAlternateContact.FullName AS CustomerAlternateContact
		--,CustomerAlternateContact.PhoneNumber AS CustomerAlternateContactPhone
		--,CustomerAlternateContact.EmailAddress AS CustomerAlternateContactEmail
		,SalesPerson.FullName AS SalesPerson
		,SalesPerson.PhoneNumber AS SalesPersonPhone
		,SalesPerson.EmailAddress AS SalesPersonEmail
		,contactPerson.FullName AS SalesOrderContact
		,contactPerson.PhoneNumber AS SalesOrderContactContactPhone
		,contactPerson.EmailAddress AS SalesOrderContactEmail
		,pickedByPerson.FullName AS PickedBy
		,pickedByPerson.PhoneNumber AS PickedByPersonPhone
		,pickedByPerson.EmailAddress AS PickedByPersonEmail
		,LastEditedBy.FullName AS LastEditedBy 
		,LastEditedBy.PhoneNumber AS LastEditedByPhone
		,LastEditedBy.EmailAddress AS LastEditedByEmail
		,o.BackorderOrderId 
		,o.IsUndersupplyBackordered
		,o.Comments
		,o.DeliveryInstructions
		,o.InternalComments
		,o.PickingCompletedWhen' 

IF EXISTS ( SELECT 1 FROM #Columns WHERE ParameterName = '@CustomerId') 
	BEGIN
		DECLARE @CustomerId NVARCHAR(MAX) = ( SELECT CONCAT('o.CustomerId = ', CONVERT(NVARCHAR(255), ParameterValue))  
											   FROM #Columns 
											   WHERE ParameterName = '@CustomerId' 
										) 
		SELECT @WhereSQL = CONCAT(
			@WhereSQL
			,CHAR(10)
			,CHAR(9)
			,'AND '
			,@CustomerId
		)
	END 

IF EXISTS ( SELECT 1 FROM #Columns WHERE ParameterName = '@OrderId') 
	BEGIN 

		DECLARE @OrderId NVARCHAR(MAX) = ( SELECT CONCAT('o.OrderId = ', CONVERT(NVARCHAR(255), ParameterValue)) 
										   FROM #Columns 
										   WHERE ParameterName = '@OrderId' 
										) 
		SELECT @WhereSQL = CONCAT(
			@WhereSQL
			,CHAR(10)
			,CHAR(9)
			,'AND '
			,@OrderId
		)
	END

SELECT @JoinSQL = CONCAT(
					 @CustomerSQL
					,CHAR(10)
					,CHAR(9)
					,@SalesPersonSQL
					,CHAR(10)
					,CHAR(9)
					,@ContactPersonSQL
					,CHAR(10)
					,CHAR(9)
					,@PickedBySQL
					,CHAR(10)
					,CHAR(9)
					,@EditedBySQL
				)

SELECT @MainSQL = CONCAT( @ColumnsSQL
			  ,CHAR(10)
			  ,@FromSQL
			  ,CHAR(10)
			  ,CHAR(9) 
			  ,@JoinSQL
			  ,CHAR(10) 
			  ,@WhereSQL
			) 

PRINT @MainSQL

EXEC(@MainSQL)

