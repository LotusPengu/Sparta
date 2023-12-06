-- For clarity, EmpOrdCount is referring to how many orders that employee is involved with
SELECT o.OrderID, o.CustomerID, o.EmployeeID, o.OrderDate,
    st.EmpOrdCount AS "Employee Order Count"
FROM Orders o
INNER JOIN(
    SELECT EmployeeID, COUNT(EmployeeID) AS "EmpOrdCount"
    FROM Orders
    GROUP BY EmployeeID
) st ON o.EmployeeID = st.EmployeeID

-- This gives the same information, but without have to conduct a JOIN
SELECT OrderID, EmployeeID,
    COUNT(*) OVER (PARTITION BY EmployeeID) AS "Employee Order Count"
FROM Orders
ORDER BY OrderID;

-- Counts the product IDs per category ID
SELECT p.ProductID, p.ProductName, 
    COUNT(ProductID) OVER (PARTITION BY p.CategoryID) - 1 AS "Count of Products in Same Category"
FROM Products p
INNER JOIN Categories c
    ON p.CategoryID = c.CategoryID
ORDER BY p.ProductID;


-- SUM is used here bc want the total number of units, not just the count
SELECT p.ProductID, p.ProductName, c.CategoryName,
    SUM(p.UnitsOnOrder) OVER (PARTITION BY c.CategoryID) AS "Total Units on Order for Category"
FROM Products p
INNER JOIN Categories c
    ON p.CategoryID = c.CategoryID
ORDER BY p.ProductID

SELECT ProductName,
    UnitPrice,
    ROW_NUMBER() OVER (ORDER BY UnitPrice DESC) AS "Row Number"
FROM Products

SELECT ProductName, UnitPrice, CategoryID,
    ROW_NUMBER() OVER (PARTITION BY CategoryID ORDER BY UnitPrice DESC) AS "Row Number"
FROM Products

-- No join req
SELECT OrderID, CustomerID, OrderDate,
    RANK() OVER (PARTITION BY CustomerID ORDER BY OrderDate ASC) AS "Order Date by Customer"
FROM Orders
ORDER BY CustomerID;

-- Code looks at the next product in the above price category
SELECT ProductName, UnitPrice
, LEAD(ProductName, 1, NULL) OVER (ORDER BY UnitPrice)
    AS "Next Product Price"
FROM Products
ORDER BY UnitPrice

-- Do not need to ORDER BY DESC as LAG() already does this, would need to add it if LEAD() was used for prev.
SELECT OrderID AS "Order ID",
    OrderDate AS "Order Date",
    Freight,
    LAG(Freight, 1, NULL) OVER (ORDER BY OrderDate) AS "Freight for Previous Order"
FROM Orders
ORDER BY [Order Date]

-- This gives the most amount of units on order for each supplier (look at supplier ID)
SELECT ProductName, SupplierID, UnitsOnOrder
,   FIRST_VALUE(UnitsOnOrder) OVER (PARTITION BY SupplierID ORDER BY UnitsOnOrder DESC)
    AS "Most Units on Order from Supplier"
FROM Products

-- No join req
-- Days since customers first order
SELECT OrderID, CustomerID, EmployeeID, OrderDate,
    DATEDIFF(DAY,
        FIRST_VALUE(OrderDate) OVER (PARTITION BY CustomerID ORDER BY OrderDate),
        GETDATE()
    ) AS "Days since customer's first order"
FROM Orders
ORDER BY OrderID

-- This code is wrong because the orderID and last order columns give the same data
SELECT OrderID, EmployeeID,
    LAST_VALUE(OrderID) OVER (PARTITION BY EmployeeID ORDER BY OrderID)
        AS 'Last Order for Employee'
FROM Orders

-- This is fixed by specifying the window clause 
-- The window clause looks at what rows it can consider 
SELECT OrderID, EmployeeID
, LAST_VALUE(OrderID) OVER (PARTITION BY EmployeeID ORDER BY OrderID
    ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)
    AS 'Last Order for Employee'
FROM Orders

-- Study moving average...
SELECT OrderID, OrderDate, Freight
, AVG(Freight) OVER (ORDER BY OrderDate
    ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING)
    AS '3pt Moving Avg'
FROM Orders

-- This uses a subquery since all the info is in one table
-- BUT we want to add the average unit price 
SELECT p.ProductName
FROM Products p
INNER JOIN (
    SELECT CategoryID
    FROM Products
    GROUP BY CategoryID
    HAVING AVG(UnitPrice) > 30
) m
    ON p.CategoryID = m.CategoryID
ORDER BY ProductName

-- The above query can be made easier by using WITH which allows us to reference a temp table
WITH MeanAbove30 AS (
    SELECT CategoryID
    FROM Products
    GROUP BY CategoryID
    HAVING AVG(UnitPrice) > 30
)
SELECT ProductName
FROM Products p
INNER JOIN
    MeanAbove30 m 
    ON p.CategoryID = m.CategoryID
ORDER BY ProductName
-- This produces a temporary table

-- This changes the data from wide to long format
-- Instead of having seperate columns for phone and fax, can combine it into one
-- Specify what data you want to go in the combined row you are creating
SELECT CompanyName, ContactType, ContactNumber
FROM Customers
UNPIVOT (ContactNumber FOR ContactType IN (Phone, Fax)) u