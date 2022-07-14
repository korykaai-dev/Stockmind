import datetime as dt
from pandas_datareader import data as pdr
import yfinance as yf

yf.pdr_override()

stock = input("Please enter a stock ticker symbol:")
print(stock)

start_year = 2019
start_month = 1
start_day = 1

start = dt.datetime(start_year, start_month, start_day)
now = dt.datetime.now()

df = pdr.get_data_yahoo(stock, start, now)

ma = 50

smaString = "Sma_" + str(ma)

df[smaString] = df.iloc[:, 4].rolling(window=ma).mean()

df = df.iloc[ma:]

numH = 0
numC = 0

for i in df.index:
    if df["Adj Close"][i] > df[smaString][i]:
        print("The close is higher")
        numH += 1
    else:
        print("The close is lower")
        numC += 1

print("Higher: " + str(numH))
print("Lower: " + str(numC))
