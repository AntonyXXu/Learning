USE AP

SELECT [VendorID]
      ,[LastName]
      ,[FirstName]
	  , LEFT(FirstName,1) + LEFT(LastName,1) AS Initials
FROM AP.dbo.ContactUpdates

SELECT InvoiceDate, 
	GETDATE() AS Today, 
	DATEDIFF(YEAR, InvoiceDate, GETDATE()) AS InvoiceAge
FROM Invoices