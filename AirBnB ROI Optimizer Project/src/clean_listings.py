import pandas as pd
import numpy as np

def clean_listings(filepath):
    df = pd.read_csv(filepath, low_memory=False)

    # ✅ These are the columns we confirmed actually exist
    cols = [
        'id', 'name', 'host_id', 'neighbourhood', 'latitude', 'longitude',
        'room_type', 'price', 'minimum_nights', 'number_of_reviews',
        'reviews_per_month', 'availability_365'
    ]
    df = df[cols]

    # ✅ Clean price column (raw string to avoid warning)
    df['price'] = df['price'].replace(r'[\$,]', '', regex=True).astype(float)

    # ✅ Estimate occupancy rate
    df['occupancy_rate'] = df['reviews_per_month'] / 30
    df['occupancy_rate'] = df['occupancy_rate'].clip(upper=1.0).fillna(0.5)

    # ✅ Estimate monthly revenue
    df['estimated_monthly_revenue'] = (
        df['price'] * (df['availability_365'] / 12) * df['occupancy_rate']
    )

    return df
