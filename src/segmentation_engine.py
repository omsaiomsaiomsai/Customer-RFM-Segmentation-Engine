import pandas as pd

def calculate_rfm(df):
    print("🧮 Calculating Recency, Frequency, and Monetary values...")
    snapshot_date = df['TransactionDate'].max() + pd.Timedelta(days=1)
    
    rfm_df = df.groupby('CustomerID').agg({
        'TransactionDate': lambda x: (snapshot_date - x.max()).days,
        'OrderID': 'count',
        'TotalAmount': 'sum'
    }).reset_index()
    
    rfm_df.rename(columns={
        'TransactionDate': 'Recency',
        'OrderID': 'Frequency',
        'TotalAmount': 'Monetary'
    }, inplace=True)
    
    print("🎯 Assigning RFM Scores (Quantiles 1-5)...")
    rfm_df['R_Score'] = pd.qcut(rfm_df['Recency'], q=5, labels=[5, 4, 3, 2, 1]).astype(int)
    rfm_df['F_Score'] = pd.qcut(rfm_df['Frequency'].rank(method='first'), q=5, labels=[1, 2, 3, 4, 5]).astype(int)
    rfm_df['M_Score'] = pd.qcut(rfm_df['Monetary'], q=5, labels=[1, 2, 3, 4, 5]).astype(int)
    
    rfm_df['RFM_Segment_Code'] = (
        rfm_df['R_Score'].astype(str) + 
        rfm_df['F_Score'].astype(str) + 
        rfm_df['M_Score'].astype(str)
    )
    return rfm_df

def assign_business_segments(rfm_df):
    print("🏷️ Mapping scores to Corporate Business Segments...")
    
    def segment_mapping(row):
        r, f = row['R_Score'], row['F_Score']
        if r >= 4 and f >= 4: return "Champions (Core High Value)"
        elif r >= 3 and f >= 3: return "Loyal Customers"
        elif r >= 4 and f <= 2: return "Recent New Customers"
        elif r <= 2 and f >= 3: return "At Risk (Can't Lose Them)"
        elif r <= 1: return "Hibernating / Lost"
        else: return "About to Sleep / Mid-Tier"

    rfm_df['Customer_Segment'] = rfm_df.apply(segment_mapping, axis=1)
    return rfm_df