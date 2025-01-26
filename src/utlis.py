import numpy as np

def backtest_portfolio(weights, returns):
	portfolio_returns = np.sum(return * weights, axis = 1)
	return portfolio_returns

def plot_results(backtest_portfolio):
	import matplotlib.pyplot as plt
	plt.plot(backtest_portfolio)
	plt.title("Portfolio performance")
	plt.show()
