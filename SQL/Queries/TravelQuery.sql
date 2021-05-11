USE TravelExperts

SELECT ProdName, PkgName
FROM Products
	JOIN Products_Suppliers on Products.ProductId = Products_Suppliers.ProductId
	JOIN Packages_Products_Suppliers as PPS on PPS.ProductSupplierId = Products_Suppliers.ProductSupplierId
	JOIN Packages on Packages.PackageId = PPS.PackageId
	WHERE ProdName = 'Travel Insurance'

--huge join statement

SELECT  AgtFirstName + ' ' + AgtLastName as Name, RegionName, Description, Destination, FeeAmt, RwdName
FROM Agents
	JOIN Customers ON Customers.AgentId = Agents.AgencyId
		JOIN Customers_Rewards on Customers.CustomerID = Customers_Rewards.CustomerId
		JOIN Rewards ON Customers_Rewards.RewardId = Rewards.RewardId
	JOIN Bookings ON Customers.CustomerID = Bookings.CustomerId
		JOIN BookingDetails ON BookingDetails.BookingID = Bookings.BookingID
		JOIN Regions ON Regions.RegionID = BookingDetails.RegionId
		JOIN Fees ON Fees.FeeID = BookingDetails.FeeID
WHERE (AgtFirstName LIKE 'b%' OR AgtLastName LIKE '%a%') AND DESTINATION <> ''
ORDER BY Name ASC


SELECT  SUM(FeeAmt) as Total, Count(FeeAmt) as Num
FROM Agents
	JOIN Customers ON Customers.AgentId = Agents.AgencyId
		JOIN Customers_Rewards on Customers.CustomerID = Customers_Rewards.CustomerId
		JOIN Rewards ON Customers_Rewards.RewardId = Rewards.RewardId
	JOIN Bookings ON Customers.CustomerID = Bookings.CustomerId
		JOIN BookingDetails ON BookingDetails.BookingID = Bookings.BookingID
		JOIN Regions ON Regions.RegionID = BookingDetails.RegionId
		JOIN Fees ON Fees.FeeID = BookingDetails.FeeID
WHERE (AgtFirstName + ' ' + AgtLastName = 'Janice Dahl') AND FeeAmt > 0


SELECT [CustCity] AS City, Count(CustomerID)
FROM Customers
GROUP BY [CustCity]

SELECT COUNT(ProductID) as Total, SupName
FROM Suppliers
	JOIN Products_Suppliers ON Products_Suppliers.SupplierID = Suppliers.SupplierId
GROUP BY Suppliers.SupName
HAVING COUNT(ProductID) > 1