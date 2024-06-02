# Restaurant Management Data Analysis Project

The Restaurant Management Data Analysis project leverages SQL for data extraction and Python for data processing and visualization to provide comprehensive insights into various aspects of a restaurant's operations. This project aims to help restaurant managers and stakeholders make informed decisions based on data-driven analysis.

## Objectives

- **Data Extraction:** Utilize SQL queries to extract meaningful data from a MySQL database, covering various facets of restaurant management.
- **Data Processing:** Employ Python, specifically the Pandas library, to process and organize the data retrieved from SQL queries.
- **Data Visualization:** Create clear and insightful visualizations using Matplotlib and Seaborn to represent the data analysis results effectively.

## Key Analysis Areas

1. **Menu Item Ingredients Distribution:** Understand the variety and frequency of ingredients used in different menu items.
2. **Customer Loyalty Program Distribution:** Analyze the distribution of customers across different loyalty program tiers.
3. **Total Completed Order Price:** Calculate the total revenue generated from completed orders.
4. **Staff Work Schedule Distribution:** Examine the distribution of staff schedules to optimize workforce management.
5. **Maximum Staff Pay Rate:** Identify the highest pay rates among the staff to understand wage distribution.
6. **Most Ordered Menu Item:** Determine which menu items are most popular among customers.
7. **Customer Reservations:** Analyze customer reservation patterns and frequencies.
8. **Menu Items with Chicken:** Identify menu items that include chicken as an ingredient.
9. **Table with Most Reservations:** Determine which tables are most frequently reserved.
10. **Customer with Most Orders:** Identify customers who place the highest number of orders.

# Skills
  
**Python**  
**SQL**  

## Entities and Attributes

1. **Customer**
   - Customer name
   - Customer contact information
   - Customer order history
   - Customer loyalty program status

2. **Menu Item**
   - Menu name
   - Menu description
   - Menu price
   - Menu ingredients
   - Menu allergens

3. **Order**
   - Items ordered
   - Quantity
   - Total price
   - Time and date of the order
   - Payment method

4. **Reservation**
   - Date and time of reservation
   - Number of guests
   - Table number
   - Special requests

5. **Staff**
   - Staff name
   - Staff contact information
   - Staff role
   - Staff schedule
   - Staff pay rate

6. **Table**
   - Table number
   - Table capacity
   - Table location
   - Table status

7. **Payment**
   - Payment time and date
   - Payment amount
   - Payment method
   - Discounts or promotions applied

## Relationships

1. One order can have many menu items (one-to-many relationship).
2. One menu item can be included in many orders (one-to-many relationship).
3. One reservation can be made by one customer (one-to-many relationship).
4. One staff member can serve many reservations (one-to-many relationship).
5. One supplier can supply many menu items (one-to-many relationship).
6. One payment can be made by one customer (one-to-many relationship).
7. A menu item can have many orders and an order can have many menu items (many-to-many relationship).
8. A reservation can have one table and a table can be associated with many reservations (one-to-many relationship).

After filling data in the following tables following functional dependencies are observed.

## Functional Dependencies and Normalisation

1. **Customer**
   - ID → First Name, Email Address, Phone Number, Loyalty Program
   - Email Address → ID
   - Phone Number → ID

2. **Order**
   - ID → Customer ID, Order date, Payment Method, Total Price, Status
   - ID → Name, Description, Price

3. **Order Item**
   - Order ID → Menu Item ID, Quantity

4. **Menu Item**
   - ID → Name, Description, Price

5. **Reservation**
   - ID → Customer ID, Date/Time, Num Guests, Table Number, VIP

6. **Table**
   - ID → Table Number, Capacity

7. **Table Status**
   - ID → Status

8. **Staff**
   - ID → First Name, Last Name, Email Address, Phone No., Schedule, Payrate
   - Email Address → ID
   - Phone Number → ID

9. **Supplier**
   - ID → Supplier Name, Email Address, Phone Number, Product List, Price List, Delivery Schedule

10. **Payment**
    - ID → Payment Date, Payment Method, Payment Amount, Offer, Payment Status
    - Customer ID → ID

All the tables which are in [create_tables.sql](https://github.com/vineeth191004/Comprehensive-Data-Analysis-and-Visualization-for-a-Restaurant-Management-System/blob/main/create_tables.sql) file are normalised upto BCNF. 

## Data Visualization
Data is visualized using Python libraries (`matplotlib` and `seaborn`). Various plots are created to represent different aspects of the data:
- **Bar Plots**: For categorical data distribution and comparisons.
- **Pie Charts**: For showing proportions of categorical data.
- **Count Plots**: For displaying frequency counts of categorical data.



