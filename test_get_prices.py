import yfinance as yf

msft = yf.Ticker("MSFT")

# for item in msft.info.items():
#     print(item)

hist = msft.history(period="1mo")
print(hist.head())
