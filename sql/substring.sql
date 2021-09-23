DECLARE @FullName VARCHAR(255) = 'Kayla Woodcock'

-- Basic Substrings 

SELECT SUBSTRING(@FullName, CHARINDEX(SPACE(1), @FullName), LEN(@FullName))
	, CHARINDEX('oo', @FullName)
	
-- Substring as a set, with CHAR INDEX 

SELECT TOP 100 
	    FullName
	   ,PreferredName
	   ,SearchName
	   ,SUBSTRING(FullName, CHARINDEX(PreferredName, FullName), LEN(PreferredName))
	   ,CHARINDEX(PreferredName, FullName)
FROM [application].people p

-- Split a string using STRING Split.

SELECT TOP 1 LTRIM(RTRIM([value] )) AS v 
FROM STRING_SPLIT(@FullName, SPACE(1))


-- Split full name and last name with space delimiter.

SELECT SUBSTRING(@FullName, 0, CHARINDEX(SPACE(1), @FullName) ) AS FirstName 
	  ,SUBSTRING(@FullName, CHARINDEX(SPACE(1), @FullName), LEN(@FullName)) AS LastName 	  
