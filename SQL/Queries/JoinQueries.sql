
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
FROM 