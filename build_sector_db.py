
import os
import pandas as pd
import yfinance as yf
import sqlite3

SECTORS = 'sectors.csv'
DATABASE = 'sector.db'

def create_connection(dbfile):
    """Function to create an sqlite3 database."""
    connection = None
    try:
        connection = sqlite3.connect(dbfile)
        return connection
    except sqlite3.Error as err:
        print(err)

def add_df_to_database(connection, df):
    """Add a Pandas dataframe to a database as a table."""
    df.to_sql(df.name, con=connection, if_exists='replace')

def add_csv_to_database(connection, csv_file):
    """Add a csv to a database as a table."""
    name = os.path.splitext(csv_file)[0]
    df = pd.read_csv(csv_file)
    df.name = name
    add_df_to_database(connection, df)

def get_stock_data_as_df(ticker_symbol, period='10y'):
    stock = yf.Ticker(ticker_symbol)
    df = stock.history(period=period)
    return df['Close']

def get_sector_stock_data_as_df(ticker_symbols, period='10y'):
    tickers = " ".join(ticker_symbols)
    df = yf.download(tickers, period=period)
    return df['Close']

def get_sector_list(conn, query):
    cursor = conn.cursor()
    conn.row_factory = lambda cursor, row: row[0]
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

def get_sector_stock_list(conn, sector_name, query):
    cursor = conn.cursor()
    conn.row_factory = lambda cursor, row: row[0]
    cursor = conn.cursor()
    full_query = "{}{}{}".format(query, sector_name, "';")
    cursor.execute(full_query)
    return cursor.fetchall()
period = '30y'
conn = create_connection(DATABASE)
add_csv_to_database(conn, SECTORS)
sector_query = "SELECT DISTINCT sector FROM sectors"
sector_list = get_sector_list(conn, query=sector_query)

# Get benchmark price data from Vanguard S&P 500 Index Fund ETF (VOO)
sp500_df = get_sector_stock_data_as_df(ticker_symbols=['VOO'], period=period)
print(sp500_df.head())

sector_stock_query = "SELECT ticker_symbol FROM sectors WHERE sector='"
for sector_name in sector_list:
    sector_stock_list = get_sector_stock_list(conn, sector_name=sector_name, query=sector_stock_query)
    df = get_sector_stock_data_as_df(ticker_symbols=sector_stock_list, period=period)
    df['sp500'] = sp500_df
    df.name = sector_name
    add_df_to_database(conn, df)

res = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
for name in res:
    print(name)

# region For sector in sectors, retrieve historical data from Yahoo Finance, add to database

# endregion
################################################################################################
# # database
# DATABASE = 'data.db'
#
# # queries
# CREATE_TABLE = "CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT)"
# CREATE_ENTRY = "INSERT INTO entries VALUES (?, ?)"
# RETRIEVE_ENTRIES = "SELECT * FROM entries"

# def get_db():
#     """Connect to the sqlite3 database"""
#     db_connection = getattr(g, '_database', None)
#     if db_connection is None:
#         db_connection = g._database = sqlite3.connect(DATABASE)
#     return db_connection
#
# def create_tables():
#     """Create database tables"""
#     with sqlite3.connect(DATABASE) as connection:
#         connection.execute(CREATE_TABLE)
#
#
# def create_entry(content, date):
#     with sqlite3.connect(DATABASE) as connection:
#         connection.execute(CREATE_ENTRY, (content, date))
#
# def retrieve_entries():
#     with sqlite3.connect(DATABASE) as connection:
#         cursor = connection.cursor()
#         cursor.execute(RETRIEVE_ENTRIES)
#         return cursor.fetchall()