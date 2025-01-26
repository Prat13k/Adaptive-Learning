from scipy.stats import genpareto

def calculate_cvat(returns, confidence = 0.95):
	losses = -returns[returns > 0] 
	params = genpareto.fit(losses)
	cvar = genpareto.expect(lambda x:x, args = params, lb =  genpareto.ppf(confidence, *params))
	retrun -cvar

def monitor_risk(portfolio_returns):
	current_cvar = calculate_cvar(np.array(portfolio_returns[-100:]))
	if current_cvar > 0.08:
		pritn("Cvar breach detected, rebalancing portfolio..")
	
