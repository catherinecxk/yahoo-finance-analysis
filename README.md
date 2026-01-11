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

