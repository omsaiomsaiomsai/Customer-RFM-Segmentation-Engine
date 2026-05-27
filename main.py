import os
from src.ingestion import fetch_transaction_data
from src.transformation import process_raw_data
from src.segmentation_engine import calculate_rfm, assign_business_segments

def run_pipeline():
    os.makedirs("data/processed", exist_ok=True)
    print("🚀 Starting Marketing RFM Data Pipeline...")
    
    raw_orders = fetch_transaction_data()
    if raw_orders:
        cleaned_df = process_raw_data(raw_orders)
        rfm_metrics = calculate_rfm(cleaned_df)
        final_portfolio_data = assign_business_segments(rfm_metrics)
        
        output_path = "data/processed/rfm_segmented_output.csv"
        final_portfolio_data.to_csv(output_path, index=False)
        print(f"\n📦 Success! Output dataset saved to: {output_path}")
    else:
        print("❌ Pipeline aborted.")

if __name__ == "__main__":
    run_pipeline()