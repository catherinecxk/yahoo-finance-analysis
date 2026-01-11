from pathlib import Path
import pandas as pd

xlsx = Path('yahoo_data.xlsx')
csv = Path('yahoo_data.csv')

if csv.exists():
	df = pd.read_csv(csv)
else:
	try:
		df = pd.read_excel(xlsx, sheet_name='Sheet1', engine='openpyxl')
	except Exception:
		df = pd.read_excel(xlsx, sheet_name='Sheet1')

# Display basic information about the DataFrame
print(df.head())
print(df.shape)
print(df.columns)
print(df.describe())

df.drop_duplicates(inplace=True)

df.rename(columns={"Close*": "Close", "Adj Close**": "Adj Close"}, inplace=True)

# How the stock value evolved over time
avg_price_by_year = df.groupby("Year")["Close"].mean()
print(avg_price_by_year)


# Identify the highest and lowest closing prices (most expensive books)
print("Highest closing price:", df["Close"].max())
print("Lowest closing price:", df["Close"].min())

# Measure the volatility of the stock each year --> More volatile means riskier
volatility_by_year = df.groupby("Year")["Close"].std()
print(volatility_by_year)

# Average closing price by month across all years --> Determines which months perform better
df["Month"] = pd.to_datetime(df["Date"]).dt.month
avg_price_by_month = df.groupby("Month")["Close"].mean()
print(avg_price_by_month)

# Average trading volume by year --> Indicates liquidity
avg_volume_by_year = df.groupby("Year")["Volume"].mean()
print(avg_volume_by_year)

# Daily returns to assess day-to-day performance
df["Daily Return"] = df["Close"].pct_change()

print("Best day:", df["Daily Return"].max())
print("Worst day:", df["Daily Return"].min())






# Save cleaned DataFrame to a new CSV file
cleaned_csv = Path('yahoo_data_cleaned.csv')
df.to_csv(cleaned_csv, index=False)



