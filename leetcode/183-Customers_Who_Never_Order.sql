# Select Customers.Name as Customers FROM Customers INNER JOIN Orders WHERE Orders.CustomerId = Customers.Id;
SELECT Name as Customers From Customers WHERE Id not in (SELECT CustomerId FROM Orders);
