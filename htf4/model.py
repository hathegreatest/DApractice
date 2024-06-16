import pandas as pd
import numpy as np
stock = pd.read_csv('HPG Historical Data.csv')
stock['Date'] = pd.to_datetime(stock['Date'])
stock = stock.sort_values(by='Date')
stock = stock.set_index('Date')
stock['Price'] = stock['Price'].str.replace(',', '').astype(float)
stock['Open'] = stock['Open'].str.replace(',', '').astype(float)
stock['High'] = stock['High'].str.replace(',', '').astype(float)
stock['Low'] = stock['Low'].str.replace(',', '').astype(float)
stock['Vol.'] = stock['Vol.'].str.replace('M', '').astype(float)
stock['Change %'] = stock['Change %'].str.replace('%', '').astype(float)
