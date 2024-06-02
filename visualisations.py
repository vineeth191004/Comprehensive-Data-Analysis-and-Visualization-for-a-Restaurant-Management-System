import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to the MySQL database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='Vineeth04!',
                             database='project',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

# Define queries
queries = [
    # QUERY 1: Menu Item Ingredients Distribution
    "SELECT MenuItem.Name, MenuItemIngredient.Ingredient FROM MenuItem JOIN MenuItemIngredient ON MenuItem.ID = MenuItemIngredient.MenuItemID",

    # QUERY 2: Customer Loyalty Program Distribution
    "SELECT LoyaltyProgram, COUNT(*) AS Count FROM Customer WHERE LoyaltyProgram = 'Gold'",

    # QUERY 3: Total Completed Order Price
    "SELECT 'Total Completed Order Price' AS Metric, SUM(TotalPrice) AS Value FROM ORDERS WHERE OrderStatus = 'Completed'",

    # QUERY 4: Staff Work Schedule Distribution
    "SELECT SCHEDULE, COUNT(*) AS Count FROM Staff WHERE SCHEDULE LIKE '%Thursday%' OR SCHEDULE LIKE '%Friday%' OR SCHEDULE LIKE '%Saturday%' OR SCHEDULE LIKE '%Sunday%' GROUP BY SCHEDULE",

    # QUERY 5: Maximum Staff Pay Rate
    "SELECT 'Max Pay Rate' AS Metric, MAX(payrate) AS Value FROM Staff",

    # QUERY 6: Most Ordered Menu Item
    "SELECT MenuItem.Name AS Menu_Item, COUNT(OrderItem.MenuItemID) AS Total_Orders FROM MenuItem JOIN OrderItem ON MenuItem.ID = OrderItem.MenuItemID GROUP BY OrderItem.MenuItemID ORDER BY Total_Orders DESC LIMIT 1",

    # QUERY 7: Customer Reservations
    "SELECT DISTINCT Customer.FirstName, Customer.EmailAddress FROM Customer JOIN Reservation ON Customer.ID = Reservation.CustomerID;",

    # QUERY 8: Menu Items with Chicken
    "SELECT Name, Description, Price FROM MenuItem WHERE ID IN (SELECT DISTINCT MenuItemID FROM MenuItemIngredient WHERE Ingredient = 'Chicken')",

    # QUERY 9: Table with Most Reservations
    "SELECT TableNumber, COUNT(ID) AS TotalReservations FROM Reservation GROUP BY TableNumber ORDER BY TotalReservations DESC LIMIT 1",

    # QUERY 10: Customer with Most Orders
    "SELECT CustomerID, COUNT(ID) AS TotalOrders FROM ORDERS GROUP BY CustomerID ORDER BY TotalOrders DESC LIMIT 1"
]

# Execute queries and store results in a dictionary
results = {}
with connection.cursor() as cursor:
    for i, query in enumerate(queries, 1):
        cursor.execute(query)
        results[f"query_{i}"] = cursor.fetchall()

# Close the connection
connection.close()

# Visualizations
for query, data in results.items():
    if "Ingredient" in data[0]:
        # Menu Item Ingredients Distribution
        df = pd.DataFrame(data)
        plt.figure(figsize=(10, 6))
        sns.countplot(y="Ingredient", data=df, order=df['Ingredient'].value_counts().index)
        plt.title("Menu Item Ingredients Distribution")
        plt.xlabel("Count")
        plt.ylabel("Ingredient")
        plt.tight_layout()
        plt.show()
    elif "LoyaltyProgram" in data[0]:
        # Customer Loyalty Program Distribution
        df = pd.DataFrame(data)
        plt.figure(figsize=(8, 8))
        plt.pie(df['Count'], labels=df['LoyaltyProgram'], autopct='%1.1f%%', startangle=140)
        plt.title("Customer Loyalty Program Distribution")
        plt.axis('equal')
        plt.tight_layout()
        plt.show()
    elif "Total Completed Order Price" in data[0]:
        # Total Completed Order Price
        df = pd.DataFrame(data)
        plt.figure(figsize=(6, 4))
        sns.barplot(x="Metric", y="Value", data=df)
        plt.title("Total Completed Order Price")
        plt.xlabel("")
        plt.ylabel("Total Price")
        plt.tight_layout()
        plt.show()
    elif "SCHEDULE" in data[0]:
        # Staff Work Schedule Distribution
        df = pd.DataFrame(data)
        plt.figure(figsize=(8, 8))
        plt.pie(df['Count'], labels=df['SCHEDULE'], autopct='%1.1f%%', startangle=140)
        plt.title("Staff Work Schedule Distribution")
        plt.axis('equal')
        plt.tight_layout()
        plt.show()
    elif "Metric" in data[0] and "Value" in data[0]:
        # Maximum Staff Pay Rate or Customer Reservations
        df = pd.DataFrame(data)
        plt.figure(figsize=(6, 4))
        sns.barplot(x="Metric", y="Value", data=df)
        plt.title(df['Metric'][0])
        plt.xlabel("")
        plt.ylabel(df['Metric'][0])
        plt.tight_layout()
        plt.show()
    elif "Menu_Item" in data[0]:
        # Most Ordered Menu Item
        df = pd.DataFrame(data)
        plt.figure(figsize=(10, 6))
        sns.barplot(x="Total_Orders", y="Menu_Item", data=df)
        plt.title("Most Ordered Menu Item")
        plt.xlabel("Total Orders")
        plt.ylabel("Menu Item")
        plt.tight_layout()
        plt.show()
    elif "FirstName" in data[0]:
        # Customer Reservations
        df = pd.DataFrame(data)
        df['ReservationCount'] = df.groupby('FirstName')['EmailAddress'].transform('count')
        df = df.drop_duplicates(subset=['FirstName', 'ReservationCount'])  # Drop duplicate rows

        plt.figure(figsize=(10, 6))
        sns.barplot(x="ReservationCount", y="FirstName", data=df)
        plt.title("Customer Reservations")
        plt.xlabel("Reservation Count")
        plt.ylabel("Customer First Name")
        plt.tight_layout()
        plt.show()

    elif "Name" in data[0]:
        # Menu Items with Chicken
        df = pd.DataFrame(data)
        plt.figure(figsize=(10, 6))
        sns.barplot(x="Price", y="Name", data=df)
        plt.title("Menu Items with Chicken")
        plt.xlabel("Price")
        plt.ylabel("Menu Item")
        plt.tight_layout()
        plt.show()
    elif "TableNumber" in data[0]:
        # Table with Most Reservations
        df = pd.DataFrame(data)
        plt.figure(figsize=(8, 6))
        sns.barplot(x="TotalReservations", y="TableNumber", data=df)
        plt.title("Table with Most Reservations")
        plt.xlabel("Total Reservations")
        plt.ylabel("Table Number")
        plt.tight_layout()
        plt.show()
    elif "CustomerID" in data[0]:
        # Customer with Most Orders
        df = pd.DataFrame(data)
        plt.figure(figsize=(8, 6))
        sns.barplot(x="TotalOrders", y="CustomerID", data=df)
        plt.title("Customer with Most Orders")
        plt.xlabel("Total Orders")
        plt.ylabel("Customer ID")
        plt.tight_layout()
        plt.show()

