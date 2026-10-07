CREATE DATABASE ecommerce_analysis;

USE ecommerce_analysis;

CREATE TABLE ecommerce_sales (
    Order_ID VARCHAR(20),
    Order_Date DATE,
    Customer_ID VARCHAR(20),
    Product VARCHAR(50),
    Category VARCHAR(50),
    Region VARCHAR(20),
    Quantity INT,
    Unit_Price DECIMAL(10,2),
    Discount DECIMAL(5,2),
    Cost DECIMAL(10,2),
    Sales DECIMAL(12,2),
    Profit DECIMAL(12,2),
    Payment_Mode VARCHAR(30)
);

SELECT COUNT(*) AS total_rows
FROM ecommerce_sales;

---  KPI Query

SELECT
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    COUNT(Order_ID) AS Total_Orders,
    SUM(Quantity) AS Total_Quantity,
    AVG(Sales) AS Average_Order_Value
FROM ecommerce_sales;

--- Product-wise Sales

SELECT
    Product,
    SUM(Sales) AS Total_Sales
FROM ecommerce_sales
GROUP BY Product
ORDER BY Total_Sales DESC;


--- Category-wise Sales

SELECT
    Category,
    SUM(Sales) AS Total_Sales
FROM ecommerce_sales
GROUP BY Category
ORDER BY Total_Sales DESC;

--- Region-wise Sales

SELECT
    Region,
    SUM(Sales) AS Total_Sales
FROM ecommerce_sales
GROUP BY Region
ORDER BY Total_Sales DESC;

--- Monthly Sales Trend

SELECT
    MONTH(Order_Date) AS Month_Number,
    MONTHNAME(Order_Date) AS Month,
    SUM(Sales) AS Total_Sales
FROM ecommerce_sales
GROUP BY MONTH(Order_Date), MONTHNAME(Order_Date)
ORDER BY Month_Number;

--- Profit by Category

SELECT
    Category,
    SUM(Profit) AS Total_Profit
FROM ecommerce_sales
GROUP BY Category
ORDER BY Total_Profit DESC;

--- Payment Mode Analysis

SELECT
    Payment_Mode,
    SUM(Sales) AS Total_Sales
FROM ecommerce_sales
GROUP BY Payment_Mode
ORDER BY Total_Sales DESC;

--- Top 10 Customers by Sales

SELECT
    Customer_ID,
    SUM(Sales) AS Total_Sales
FROM ecommerce_sales
GROUP BY Customer_ID
ORDER BY Total_Sales DESC
LIMIT 10;

--- Discount Analysis

SELECT
    Discount,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM ecommerce_sales
GROUP BY Discount
ORDER BY Discount;


