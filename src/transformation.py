import pandas as pd

def process_raw_data(raw_orders):
    print("⚙️ Processing and cleaning raw JSON data...")
    parsed_records = []
    
    for order in raw_orders:
        customer = order.get('customer', {})
        customer_id = customer.get('id')
        if not customer_id:
            continue
            
        parsed_records.append({
            'CustomerID': int(customer_id),
            'OrderID': int(order.get('id')),
            'TransactionDate': order.get('created_at'),
            'TotalAmount': float(order.get('total_price', 0.0))
        })
        
    df = pd.DataFrame(parsed_records)
    df['TransactionDate'] = pd.to_datetime(df['TransactionDate']).dt.tz_localize(None)
    df = df[df['TotalAmount'] > 0]
    print("✅ Data cleaned and formatted into a DataFrame.")
    return df