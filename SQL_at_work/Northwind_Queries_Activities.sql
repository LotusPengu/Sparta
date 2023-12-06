-- "Total Price" is created as a SELECT subqeury in the JOIN clause
-- This is then JOINED onto the Orders table
-- Within the primary SELECT clause, we specify the window function 
SELECT o.OrderID, o.OrderDate, d.[Total Price]
, AVG(d.[Total Price]) OVER (ORDER BY o.OrderDate
ROWS BETWEEN 2 PRECEDING AND 2 FOLLOWING) AS "5pt Moving Average"
FROM Orders o
JOIN (
    SELECT OrderID,
    SUM(UnitPrice*Quantity*(1-Discount)) AS "Total Price"
    FROM [Order Details]
    GROUP BY OrderID
) d ON o.OrderID = d.OrderID

SELECT OrderID, DateType, Date
INTO #OrderDates
FROM Orders o
UNPIVOT (Date FOR DateType IN (OrderDate, RequiredDate, ShippedDate)) d

-- Input the columns in the opposite order, also ensure to add MAX( )
SELECT OrderID, OrderDate, RequiredDate, ShippedDate
FROM #OrderDates 
PIVOT (MAX(Date) FOR DateType IN (OrderDate, RequiredDate, ShippedDate)) d

SELECT FirstName +' '+ LastName AS "Employee Name"
FROM Employees

-- Selects regions that only use two letters in their code
SELECT DISTINCT Region
FROM Customers
WHERE REGION IS NOT NULL AND LEN(Region) = 2;

-- Selects only countries that have a region code specified
SELECT DISTINCT Country
FROM Customers
WHERE Region IS NOT NULL;

SELECT OrderID,
    SUM(UnitPrice*Quantity*(1-Discount)) AS "Net Total"
FROM [Order Details]
GROUP BY OrderID
ORDER BY "Net Total" DESC;

SELECT DISTINCT CHARINDEX('''',ProductName) AS "SingleQuotePosition", ProductName AS "Product Name"
FROM Products
WHERE CHARINDEX('''',ProductName) != 0;

-- Outputs the age of each employee by calculating the difference between current date and birth date
SELECT FirstName +' '+ LastName,
    DATEDIFF(Year, BirthDate, GETDATE()) AS "Age"
FROM Employees;

SELECT CategoryID,
    AVG(ReorderLevel) AS "Average Reorder Level"
FROM Products
GROUP BY CategoryID
ORDER BY "Average Reorder Level" DESC;

SELECT o.OrderID, o.OrderDate, o.Freight, c.CompanyName AS "Customer", e.Firstname +' '+ e.LastName AS "Employee Name"
FROM Orders o
JOIN Employees e
    ON o.EmployeeID = e.EmployeeID
JOIN Customers c
    ON o.CustomerID = c.CustomerID

SELECT OrderID, ProductID, UnitPrice, Discount, Quantity
FROM [Order Details]
WHERE ProductID IN(
    SELECT ProductID
    FROM Products
    WHERE Discontinued = 1
);

SELECT od.OrderID, od.ProductID, od.UnitPrice, Discount, Quantity, p.Discontinued
FROM [Order Details] od
JOIN Products p
    ON od.ProductID = p.ProductID
WHERE p.Discontinued != 0;