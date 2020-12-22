import os
import pandas as pd
import yfinance as yf
import sqlite3

brk = yf.Ticker('VOO')
hist = brk.history('10y')
print(brk.info)

