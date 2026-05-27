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