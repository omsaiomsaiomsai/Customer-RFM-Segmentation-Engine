-- 1. Create the Table Structure
CREATE TABLE CUSTOMER_RFM_METRICS (
    CustomerID NUMBER(19, 0) PRIMARY KEY,
    Recency NUMBER(10, 0),
    Frequency NUMBER(10, 0),
    Monetary NUMBER(19, 4),
    R_Score NUMBER(2, 0),
    F_Score NUMBER(2, 0),
    M_Score NUMBER(2, 0),
    RFM_Segment_Code VARCHAR2(10),
    Customer_Segment VARCHAR2(50)
);

-- 2. Executive Aggregation Query
SELECT 
    Customer_Segment,
    COUNT(CustomerID) AS Total_Customers,
    ROUND(AVG(Recency), 1) AS Avg_Days_Since_Last_Purchase,
    ROUND(AVG(Frequency), 1) AS Avg_Purchase_Frequency,
    ROUND(AVG(Monetary), 2) AS Avg_Total_Spend,
    ROUND(SUM(Monetary), 2) AS Total_Segment_Revenue
FROM 
    CUSTOMER_RFM_METRICS
GROUP BY 
    Customer_Segment
ORDER BY 
    Total_Segment_Revenue DESC;