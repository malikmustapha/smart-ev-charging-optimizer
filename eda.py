import pandas as pd

df = pd.read_csv('data/electric.csv')

# Clean column names (strip spaces)
df.columns = df.columns.str.strip()

# Remove ':00' from Hour Ending if present
df['Hour Ending'] = df['Hour Ending'].astype(str).str.replace(':00', '')

# Convert Hour Ending to int
df['Hour Ending'] = df['Hour Ending'].astype(int)

# Create datetime by combining Delivery Date and Hour Ending
df['datetime'] = pd.to_datetime(df['Delivery Date']) + pd.to_timedelta(df['Hour Ending'] - 1, unit='h')

# Use REGUP as price column (strip spaces)
df.rename(columns={'REGUP': 'price'}, inplace=True)

# Select only needed columns
df = df[['datetime', 'price']]

print(df.head())


