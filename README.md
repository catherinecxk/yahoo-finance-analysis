Financial Time-Series Analysis (2018–2023)


Overview

This project analyzes historical market data from Yahoo Finance using Python and Pandas. The goal is to explore how a financial asset’s price and trading activity changed over time, identify seasonal patterns, and measure risk through volatility and daily returns.

The project follows a full data-analysis pipeline:

Loading raw financial data

Cleaning and transforming it

Engineering new financial features

Running statistical and time-series analysis

Visualizing trends




Dataset

Source: Yahoo Finance [(via Kaggle)](https://www.kaggle.com/datasets/suruchiarora/yahoo-finance-dataset-2018-2023?resource=download)
Time period: 2018 – 2023
Frequency: Daily trading data


Each row represents one trading day and contains:
Column	-- Description
Date	-- Trading date
Open	-- Opening price
High	-- Highest price of the day
Low	-- Lowest price of the day
Close	-- Closing price
Adj Close	-- Adjusted closing price (corporate actions)
Volume	-- Number of shares traded


Key Features Added

To enable financial analysis, several new features were created:

Year – extracted from Date

Month – extracted from Date

Daily Return – percentage change in closing price


Analyses Performed
1. Price Trends Over Time

The closing price was plotted across all dates to visualize long-term growth, drawdowns, and volatility.

This reveals:

Market trends

Bull and bear periods

Large price shocks

2. Average Price by Year

The mean closing price was calculated for each year to measure long-term performance.

This answers:

Did the asset become more valuable over time?

3. Volatility by Year

Standard deviation of daily prices was computed for each year.

Higher volatility indicates:

More risk

Larger daily price swings

Unstable market conditions

4. Trading Volume Analysis

Average daily trading volume was computed by year to measure investor interest and liquidity.

Large spikes typically occur during:

Market crashes

Earnings cycles

Major news events

5. Best and Worst Trading Days

Daily percentage returns were calculated to identify:

Largest one-day gains

Largest one-day losses

This is used in:

Risk analysis

Stress testing

Portfolio management



Tech Stack

Python

Pandas

Matplotlib

Jupyter Notebook / VS Code


How to Run
1. Instal dependcies:
pip install pandas matplotlib openpyxl

2. Run the analysis:
python main.py

