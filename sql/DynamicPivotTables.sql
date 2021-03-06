USE [Consolidation]
GO
/****** Object:  StoredProcedure [dbo].[DynamicPivotTableInSql]    Script Date: 9/21/2021 9:59:03 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
ALTER   PROCEDURE [dbo].[DynamicPivotTableInSql]
    @ListToPivot    NVARCHAR(255)
	,@SQL NVARCHAR(MAX) 
	,@PivotColumn NVARCHAR(MAX)
	,@Aggregate NVARCHAR(MAX) 
	,@TableName NVARCHAR(MAX) 
AS
BEGIN
   SET NOCOUNT ON; 
  DECLARE @SqlStatement NVARCHAR(MAX)
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
  ';
  --PRINT @SqlStatement
  EXEC(@SqlStatement)
 
END
