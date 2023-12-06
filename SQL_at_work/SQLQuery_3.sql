SELECT City
FROM Employees
WHERE City = 'London';

--This is better written as...
SELECT COUNT(City) AS "London Count"
FROM Employees
WHERE City = 'London';
-- Because this puts the count value in a single column - easier to read!!

-- Make sure to check where you can find this data, and make it easy for the reader to interpret
SELECT FirstName AS "First Name", LastName AS "Last Name"
FROM Employees
WHERE TitleOfCourtesy LIKE '%Dr%'

SELECT COUNT(Discontinued) AS "Products Discontinued Count"
FROM Products
WHERE Discontinued = 1

SELECT ProductName AS "Product Name", ProductID AS "Product ID"
FROM Products
WHERE UnitPrice < 5.00;

SELECT CategoryName AS "Category Name"
FROM Categories
WHERE CategoryName LIKE 'B%' OR CategoryName LIKE 'S%';
-- Try and work backwards, especially for more complex queries, follow the processing sequence
-- Trial and error does not work for queries involved in updating and deleting, that cannot be ran again 

-- You can also do...
SELECT CategoryName AS "Category Name"
FROM Categories
WHERE CategoryName LIKE '[BS]%';

SELECT COUNT(OrderID) AS "Order Total"
FROM Orders
WHERE EmployeeID LIKE '[5,7]';

-- Discount is a percentage (e.g., 0.15) so have to multiply it to the Gross Total, (1-) so that it is not multiplying by 0
SELECT UnitPrice, Quantity, Discount,
    UnitPrice * Quantity AS "Gross Total",
    UnitPrice * Quantity * (1-Discount) AS "Net Total"
FROM [Order Details]

-- You cannot refer to column aliases if the clause is processed before where the alias is defined
-- Double quotes is used for defining column names, such as aliases, else use single quotes
SELECT FirstName + ' ' + LastName AS "Employees Name", DATEDIFF(yy,BirthDate,GETDATE()) AS "Age",
    CASE
        WHEN DATEDIFF(yy,BirthDate,GETDATE()) > 65 THEN 'Retired'
        WHEN DATEDIFF(yy,BirthDate,GETDATE()) > 60 THEN 'Retirement Due'
        ELSE 'More than 5 years to go'
    END AS "Retirement Status"
FROM Employees;

-- You may also use a subquery to reference the Age alias, rather than repeating the DATADIFF line
-- FROM is processed before SELECT which is why this works
SELECT [Employee Name], Age,
    CASE
        WHEN Age > 65
            THEN 'Retired'
        WHEN Age > 60
            THEN 'Retirement Due'
        ELSE 'More than 5 years'
    END AS "Retirement Status"
FROM (
    SELECT FirstName + ' ' + LastName AS "Employee Name",
        DATEDIFF(yy,BirthDate,GETDATE()) AS "Age"
    FROM Employees
) AS sq;

SELECT p.SupplierID AS "Supplier ID", AVG(p.UnitsOnOrder) AS "Average Units On Order", CompanyName AS "Company Name"
FROM Products p -- Product is simplified to p
INNER JOIN Suppliers s -- Supplier is simplified to s 
ON p.SupplierID = s.SupplierID -- Created an innerjoin from the p and s tables so we can access Company Name
-- This was joined using SupplierID as it is a FK thus acts as a link between the two tables
GROUP BY p.SupplierID, CompanyName

SELECT * 
FROM suppliers;
