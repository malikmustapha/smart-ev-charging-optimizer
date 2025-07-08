import pandas as pd

# Load raw data (replace with your correct path)
df = pd.read_csv('data/electric.csv')

# Clean column names (remove spaces)
df.columns = df.columns.str.strip()

# Remove ':00' from Hour Ending if present
df['Hour Ending'] = df['Hour Ending'].astype(str).str.replace(':00', '')

# Convert Hour Ending to int
df['Hour Ending'] = df['Hour Ending'].astype(int)

# Create datetime column
df['datetime'] = pd.to_datetime(df['Delivery Date']) + pd.to_timedelta(df['Hour Ending'] - 1, unit='h')

# Use REGUP as price
df.rename(columns={'REGUP': 'price'}, inplace=True)

# Keep only needed columns
df = df[['datetime', 'price']]

# Save cleaned CSV
df.to_csv('data/hourly_prices.csv', index=False)

print("✅ Preprocessing done. Saved to data/hourly_prices.csv")
