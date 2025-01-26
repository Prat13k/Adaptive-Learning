import pandas as pd
import yfinance as yf
import pandas_datareader.data as web

def fetch_macro_data():
	start_date = '2010-01-01'
	indicators = {"VIX" : "VIXCLS", "10Y - 2Y Spread":"T10Y2Y","CPI":"CPIAUCSL"}
	df = web.DataReader(list(indicators.values()))
	df.columns = list(indicators.keys())
	return df.pct_change().dropna()
	
def fetch_price_data(tickers):
	data = yf.download(tickers, start = "2010-01-01")
	return data

def preprocess_data(price_data, macro_data):
	price_data['volatility'] = price_data['SPY'].pct_change().rolling(30).std
	merged = pd.merge(price_data, macro_data, left_index = True, right_index = True)
	return merged.dropna()
