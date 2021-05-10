USE AP

SELECT InvoiceNumber, VendorName
FROM Vendors JOIN Invoices
		ON Invoices.VendorID = Vendors.VendorID

SELECT InvoiceNumber, InvoiceDate, InvoiceTotal, InvoiceLineItemAmount
FROM Invoices JOIN InvoiceLineItems
	ON (Invoices.InvoiceID = InvoiceLineItems.InvoiceID) 
	AND (Invoices.InvoiceTotal > InvoiceLineItems.InvoiceLineItemAmount)
ORDER BY InvoiceDate

-- Join More Tables
SELECT VendorName, InvoiceNumber, InvoiceDate, InvoiceLineItemAmount as Amount, AccountDescription
FROM Invoices
	JOIN Vendors ON Invoices.VendorID = Vendors.VendorID
	JOIN InvoiceLineItems ON Invoices.InvoiceID = InvoiceLineItems.InvoiceID
	JOIN GLAccounts ON InvoiceLineItems.AccountNo = GLAccounts.AccountNo
ORDER BY VendorName, InvoiceLineItemAmount DESC

--Left outer join
Select VendorName, InvoiceNumber, InvoiceTotal 
FROM Vendors
	LEFT JOIN Invoices ON Vendors.VendorID = Invoices.VendorID

--Cross Join
Select *
FROM Vendors CROSS JOIN Invoices

SELECT VendorName, InvoiceDate, InvoiceID
FROM Vendors
	JOIN Invoices ON invoices.VendorID = Vendors.VendorID
	WHERE InvoiceDate > '2016-01-01'