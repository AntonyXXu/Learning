SELECT [VendorID]
      ,[LastName]
      ,[FirstName]
	  , LEFT(FirstName,1) + LEFT(LastName,1) AS Initials
FROM AP.dbo.ContactUpdates