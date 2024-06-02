INSERT INTO Customer (ID, FirstName, EmailAddress, PhoneNumber, LoyaltyProgram)
VALUES
    (1, 'Vishal', 'vishal04@gmail.com', '9441586780', 'Gold'),
    (2, 'John', 'john.smith@gmail.com', '9876543271', 'Bronze'),
    (3, 'James', 'james@gmail.com', '9145624782', 'Silver');

INSERT INTO MenuItem (ID, Name, Description, Price)
VALUES
    (1, 'Burger', 'Classic cheeseburger', 50.0),
    (2, 'Pizza', 'Margherita pizza', 200.0),
    (3, 'Shawarma', 'Chicken Shwarma', 150.0);

INSERT INTO MenuItemIngredient (MenuItemID, Ingredient)
VALUES
    (1, 'Chicken'),
    (2, 'Tomato sauce'),
    (3, 'Chicken');

INSERT INTO ORDERS (ID, CustomerID, OrderDate, PaymentMethod, TotalPrice, OrderStatus)
VALUES
    (1, 1, '2023-03-25 18:00:00', 'Credit card', 50.0, 'Completed'),
    (2, 2, '2023-03-25 18:30:00', 'Cash', 250.0, 'Completed'),
    (3, 1, '2023-03-26 12:00:00', 'Credit card', 350.0, 'In progress');

INSERT INTO INCLUDES (OrderID, MenuItemID)
VALUES
    (1, 1),
    (2, 2),
    (3, 3);

INSERT INTO OrderItem (OrderID, MenuItemID, Quantity)
VALUES
    (1, 1, 2),
    (1, 3, 1),
    (2, 2, 1);

INSERT INTO Reservation (ID, CustomerID, DateTime, NumGuests, TableNumber, VIP)
VALUES
    (1, 2, '2023-03-27 18:00:00', 4, 2, 'Vegetarian options'),
    (2, 3, '2023-03-28 12:30:00', 2, 3, ''),
    (3, 1, '2023-03-29 19:00:00', 6, 5, 'High chair required');

INSERT INTO TABLES (ID, TableNumber, Capacity)
VALUES
    (1, 1, 4),
    (2, 2, 6),
    (3, 3, 2);

INSERT INTO TABLESTATUS (ID, Status)
VALUES
    (1, 'Available'),
    (2, 'Available'),
    (3, 'Reserved');

INSERT INTO Staff (ID, FirstName, LastName, EmailAddress, PhoneNumber, Schedule, payrate)
VALUES
    (1, 'Susheel', 'Thula', 'johndoe@example.com', '123-456-7890', 'Monday-Friday, 9am-5pm', '$20/hour'),
    (2, 'Honeysh', 'Manda', 'janedoe@example.com', '123-456-7890', 'Monday-Friday, 5pm-1am', '$25/hour'),
    (3, 'Raju', 'Samala', 'bobsmith@example.com', '123-456-7890', 'Thursday-Sunday, 5pm-10am', '$15/hour'),
    (4, 'Alice', 'Palnati', 'alicejones@example.com', '123-456-7890', 'Tuesday-Saturday, 12pm-9pm', '$25/hour');

INSERT INTO Supplier (ID, SupplierName, EmailAddress, PhoneNumber, ProductList, PriceList, DeliverySchedule)
VALUES
    (1, 'Fresh Foods Inc', 'freshfoods@gmail.com', '123-456-7890', 'Organic Tomatoes', 150.99, '2023-04-01 10:00:00'),
    (2, 'Farm to Table Produce', 'farmtotable@gmail.com', '134-456-7890', 'Fresh Salmon', 200.99, '2023-04-01 12:00:00'),
    (3, 'ABC Suppliers', 'abc@gmail.com', '256-567-7890', 'Organic Lettuce', 280.99, '2023-04-02 09:00:00');

INSERT INTO Payment (ID, CustomerID, PaymentDate, PaymentMethod, PaymentAmount, Offer, PaymentStatus)
VALUES
    (1, 1, '2023-03-25 18:00:00', 'Credit Card', 450.95, '5%', 'Paid'),
    (2, 2, '2023-03-26 12:00:00', 'Cash', 250.00, '4%', 'Paid'),
    (3, 3, '2023-03-27 13:00:00', 'Credit Card', 500.00, '3%', 'Paid');
    
    