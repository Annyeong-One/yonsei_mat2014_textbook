# Pandas Tutorial: Time Series Analysis
# Covers datetime operations, resampling, rolling windows, time zones

import pandas as pd
import numpy as np

print("="*70)
print("TIME SERIES ANALYSIS")
print("="*70)

# Create time series data
dates = pd.date_range('2024-01-01', periods=100, freq='D')
np.random.seed(42)
ts_data = pd.DataFrame({
    'Date': dates,
    'Sales': np.random.randint(100, 500, 100),
    'Temperature': np.random.uniform(15, 35, 100)
})
ts_data.set_index('Date', inplace=True)

print("\nTime Series Data:")
print(ts_data.head())

# Date parsing
print("\n1. Parse dates from strings:")
date_strings = ['2024-01-01', '2024-02-15', '2024-03-30']
parsed_dates = pd.to_datetime(date_strings)
print(parsed_dates)

# Date ranges
print("\n2. Create date ranges:")
print("Daily:", pd.date_range('2024-01-01', periods=5, freq='D'))
print("Weekly:", pd.date_range('2024-01-01', periods=5, freq='W'))
print("Monthly:", pd.date_range('2024-01-01', periods=5, freq='MS'))

# Accessing datetime components
print("\n3. Extract datetime components:")
ts_data['Year'] = ts_data.index.year
ts_data['Month'] = ts_data.index.month
ts_data['Day'] = ts_data.index.day
ts_data['DayOfWeek'] = ts_data.index.dayofweek
print(ts_data[['Sales', 'Year', 'Month', 'Day', 'DayOfWeek']].head())

# Resampling (changing frequency)
print("\n4. Resample to weekly frequency (sum):")
weekly = ts_data['Sales'].resample('W').sum()
print(weekly.head())

print("\n5. Resample to monthly (mean):")
monthly = ts_data['Sales'].resample('MS').mean()
print(monthly.head())

# Rolling windows
print("\n6. Rolling mean (7-day window):")
ts_data['Sales_MA7'] = ts_data['Sales'].rolling(window=7).mean()
print(ts_data[['Sales', 'Sales_MA7']].head(10))

print("\n7. Rolling statistics:")
rolling_stats = ts_data['Sales'].rolling(window=7).agg(['mean', 'std', 'min', 'max'])
print(rolling_stats.head(10))

# Expanding windows
print("\n8. Expanding mean (cumulative):")
ts_data['Cumulative_Mean'] = ts_data['Sales'].expanding().mean()
print(ts_data[['Sales', 'Cumulative_Mean']].head(10))

# Shift and lag
print("\n9. Shift values (lag/lead):")
ts_data['Sales_Yesterday'] = ts_data['Sales'].shift(1)
ts_data['Sales_Tomorrow'] = ts_data['Sales'].shift(-1)
print(ts_data[['Sales', 'Sales_Yesterday', 'Sales_Tomorrow']].head())

# Percentage change
print("\n10. Percentage change:")
ts_data['Sales_Pct_Change'] = ts_data['Sales'].pct_change()
print(ts_data[['Sales', 'Sales_Pct_Change']].head())

# Time zones
print("\n11. Time zone operations:")
utc_dates = pd.date_range('2024-01-01', periods=3, freq='D', tz='UTC')
print("UTC:", utc_dates)

# Convert time zone
eastern = utc_dates.tz_convert('US/Eastern')
print("Eastern:", eastern)

print("\nKEY TAKEAWAYS:")
print("- pd.to_datetime(): Parse dates from strings")
print("- pd.date_range(): Create date sequences")
print("- resample(): Change time frequency")
print("- rolling(): Moving window calculations")
print("- shift(): Lag/lead values")
print("- pct_change(): Percentage change")
print("- Time zone handling with tz parameter")