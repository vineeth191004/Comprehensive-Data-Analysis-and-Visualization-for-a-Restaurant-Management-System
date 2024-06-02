-- QUERY 1:
SELECT MenuItem.Name, MenuItemIngredient.Ingredient
FROM MenuItem
JOIN MenuItemIngredient ON MenuItem.ID = MenuItemIngredient.MenuItemID; 

-- QUERY 2:
SELECT * FROM Customer WHERE LoyaltyProgram = 'Gold'; 

-- QUERY 3:
SELECT SUM(TotalPrice) AS TotalCompletedOrderPrice FROM ORDERS WHERE OrderStatus = 'Completed';

-- QUERY 4:
SELECT * FROM Staff WHERE SCHEDULE LIKE '%Thursday%' OR SCHEDULE LIKE '%Friday%' OR SCHEDULE LIKE '%Saturday%' OR SCHEDULE LIKE '%Sunday%';

-- QUERY 5:
SELECT MAX(payrate) FROM staff; 

-- QUERY 6:
SELECT MenuItem.Name, COUNT(OrderItem.MenuItemID) AS TotalOrders
FROM MenuItem
JOIN OrderItem ON MenuItem.ID = OrderItem.MenuItemID
GROUP BY OrderItem.MenuItemID
ORDER BY TotalOrders DESC
LIMIT 1;

-- QUERY 7:
SELECT DISTINCT Customer.FirstName, Customer.EmailAddress
FROM Customer
JOIN Reservation ON Customer.ID = Reservation.CustomerID;

-- QUERY 8
SELECT Name, Description, Price
FROM MenuItem
WHERE ID IN (
  SELECT DISTINCT MenuItemID
  FROM MenuItemIngredient
  WHERE Ingredient = 'Chicken'
);

-- QUERY 9
SELECT TableNumber, COUNT(ID) AS TotalReservations
FROM Reservation
GROUP BY TableNumber
ORDER BY TotalReservations DESC
LIMIT 1;

-- QUERY 10
SELECT CustomerID, COUNT(ID) AS TotalOrders
FROM ORDERS
GROUP BY CustomerID
ORDER BY TotalOrders DESC
LIMIT 1;
