import yfinance as yf
import matplotlib.pyplot as plt

# Download historical data
ticker = input("Ticker der Aktie: ")
data = yf.download(ticker, start="2020-01-01", end="2023-03-05")

# Chart
plt.figure(figsize=(10, 5))
plt.plot(data["Close"])
plt.title(f"{ticker} Stock Chart")
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()