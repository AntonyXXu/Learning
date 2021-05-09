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

SELECT DISTINCT VendorCity, VendorState
FROM Vendors

SELECT * FROM Invoices
WHERE (InvoiceDate > '01/01/2016'
    OR InvoiceTotal > 500)
    AND InvoiceTotal - PaymentTotal - CreditTotal > 0

SELECT InvoiceNumber FROM Invoices 
WHERE InvoiceDate BETWEEN '01/01/2016' AND '04/01/2016'

SELECT VendorName, VendorCity
FROM Vendors
ORDER BY VendorName DESC