import random
from datetime import datetime, timedelta

def fetch_transaction_data():
    print("📡 Bypassing dead API... Generating local mock Shopify data.")
    
    orders = []
    # Generate 500 mock orders for RFM testing
    for i in range(1, 501):
        # Random date within the last 365 days for Recency
        random_days_ago = random.randint(0, 365)
        order_date = (datetime.now() - timedelta(days=random_days_ago)).strftime("%Y-%m-%dT%H:%M:%SZ")
        
        # Simulating standard Shopify JSON order structure
        orders.append({
            "id": 1000 + i,
            "customer": {
                "id": random.randint(1, 50) # 50 unique customers for Frequency grouping
            },
            "created_at": order_date,
            "total_price": str(round(random.uniform(15.00, 500.00), 2)) # Monetary value
        })
        
    print(f"✅ Successfully generated {len(orders)} raw mock records.")
    return orders