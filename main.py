from src.data.data_pipeline import fetch_macro_data, fetch_price_data, preprocess_data
from src.models.regime_detection import detect_regimes
from src.models.gnn_correlation import train_gnn
from src.models.rl_optimization import train_rl_agent
from src.risk.risk_management import monitor_risk

def main():
	price_data = fetch_price_data(['SPY','QQQ'])
	macro_data = fetch_macro_data()
	preprocessed_data = preprocess_data(price_data, macro_data)
	
	regime_data = detect_regimes(preprocessed_data)
	gnn_model = train_gnn(preprocessed_data['returns'],preprocessed_data['edges'])
	rl_agent = train_rl_agent(preprocess_data['returns'],preprocessed_data['regime'])
	monitor_risk(rl_agent.portfolio_returns)

if __name__ == 'main':
	main()
