import pytest
from src.data_pipeline import fetch_macro_data,fetch_price_data, preprocess_data

def test_fetch_macro_data():
	data = fetch_macro_data()
	assert not data.empty, "Macro data fetch failed"

def test_fetch_price_data():
	data = fetch_price_data(['SPY'])
	assert not data.empty,"Price data fetch failed"

def test_preprocess_data():
	price_data = fetch_price_data(['SPY')
	macro_data = fetch_macro_data()
	preprocessed = preprocess_data(price_data, macro_data)
	assert not processed.empty, "data preprocessing failed"
