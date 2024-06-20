import pandas as pd

# Sample sales data
data = {
    'Date': pd.date_range(start='2023-01-01', periods=100, freq='D'),
    'Product': ['Product A', 'Product B', 'Product C', 'Product D'] * 25,
    'Sales': pd.np.random.randint(100, 1000, size=100),
    'Region': ['North', 'South', 'East', 'West'] * 25
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('/mnt/data/sales_data.csv', index=False)
