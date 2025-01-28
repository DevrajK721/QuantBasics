# Imports 
import numpy as np 
import yfinance as yf 
import pandas as pd 
import matplotlib.pyplot as plt
import scipy.optimize as optimization 

# Stocks we are going to handle 
stocks = ['AAPL', 'WMT', 'TSLA', 'GE', 'AMZN', 'DB']

# Historical data - define START and END dates
start_date = '2012-01-01'
end_date = '2017-01-01' 
NUM_TRADING_DAYS = 252 # On average there are 252 trading days in a year
NUM_PORTFOLIOS = 10000 # Number of portfolios we are going to generate

def download_data(stocks, start_date, end_date):
    # Name of Stock: Stock Values (2010 - 2017) as the values 
    stock_data = {} # Empty dictionary to store the data
    
    for stock in stocks:
        # Closing Prices
        ticker = yf.Ticker(stock)
        stock_data[stock] = ticker.history(start=start_date, end=end_date)['Close']
        
    return pd.DataFrame(stock_data) 

def show_data(stock_data):
    plt.style.use('dark_background')
    stock_data.plot(figsize=(10, 5))
    plt.grid(True, color='lightgrey')
    plt.show()
    
def calculate_return(data):
    # ln(S(t)/S(t-1)) - log return for normalizing the data
    log_return = np.log(data / data.shift(1))
    return log_return[1:]
    
def show_statistics(returns, NUM_TRADING_DAYS):
    # Instead of using the mean, we will use the geometric mean
    return returns.mean() * NUM_TRADING_DAYS, returns.cov() * NUM_TRADING_DAYS

def show_mean_variance(returns, weights):
    portfolio_return = np.sum(returns.mean() * weights) * NUM_TRADING_DAYS
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * NUM_TRADING_DAYS, weights)))  

    return portfolio_return, portfolio_volatility

def generate_portfolios(returns, NUM_PORTFOLIOS):
    portfolio_means = []
    portfolio_risks = []
    portfolio_weights = []
    
    for _ in range(NUM_PORTFOLIOS):
        weight = np.random.random(len(stocks)) # Random weights
        weight /= np.sum(weight) # Normalize the weights 
        portfolio_weights.append(weight)
        portfolio_means.append(np.sum(returns.mean() * weight) * NUM_TRADING_DAYS)
        portfolio_risks.append(np.sqrt(np.dot(weight.T, np.dot(returns.cov() * NUM_TRADING_DAYS, weight))))
    
    return np.array(portfolio_weights), np.array(portfolio_means), np.array(portfolio_risks)

def show_portfolios(portfolio_means, portfolio_risks):
    plt.style.use('dark_background')
    plt.figure(figsize=(10, 6))
    plt.scatter(portfolio_risks, portfolio_means, c=portfolio_means/portfolio_risks, marker='o', cmap='coolwarm')
    plt.grid(True, color='lightgrey')
    plt.xlabel('Expected Volatility')
    plt.ylabel('Expected Return')
    plt.colorbar(label='Sharpe Ratio')
    plt.show()
    
def statistics(weights, returns):
    portfolio_return = np.sum(returns.mean() * weights) * NUM_TRADING_DAYS
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(returns.cov() * NUM_TRADING_DAYS, weights)))
    
    return np.array([portfolio_return, portfolio_volatility, portfolio_return / portfolio_volatility])

# Scipy Optimization can find the minimum of a given function 
def min_func_sharpe(weights, returns):
    return -statistics(weights, returns)[2]

def optimize_portfolio(weights, returns):
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    # The weights can be 1 at most and 0 at least
    bounds = tuple((0, 1) for _ in range(len(stocks)))
    return optimization.minimize(fun=min_func_sharpe, x0=weights, args=returns, method='SLSQP', bounds=bounds, constraints=constraints)

def print_optimal_portfolio(optimal_portfolio, returns):
    print("Optimal Portfolio Weights: ", optimal_portfolio['x'].round(3))
    print("Expected Portfolio Return: ", statistics(optimal_portfolio['x'], returns)[0])
    print("Expected Portfolio Volatility: ", statistics(optimal_portfolio['x'], returns)[1])
    print("Expected Portfolio Sharpe Ratio: ", statistics(optimal_portfolio['x'], returns)[2])
    
def show_optimal_portfolio(opt, rets, portfolio_rets, portfolio_vols):
    plt.style.use('dark_background')
    plt.figure(figsize=(10, 6))
    plt.scatter(portfolio_vols, portfolio_rets, c=portfolio_rets/portfolio_vols, marker='o', cmap='coolwarm')
    plt.grid(True, color='lightgrey')
    plt.xlabel('Expected Volatility')
    plt.ylabel('Expected Return')
    plt.colorbar(label='Sharpe Ratio')
    plt.plot(statistics(opt['x'], rets)[1], statistics(opt['x'], rets)[0], 'g*', markersize=20.0)
    plt.show()

if __name__ == '__main__':
    stock_data = download_data(stocks, start_date, end_date)
    show_data(stock_data)
    
    returns = calculate_return(stock_data)
    mean, variance = show_statistics(returns, NUM_TRADING_DAYS)
    
    weights = np.random.random(len(stocks))
    weights /= np.sum(weights)
    
    print("Mean: ", mean)
    print("Variance: ", variance)
    
    portfolio_weights, portfolio_means, portfolio_risks = generate_portfolios(returns, NUM_PORTFOLIOS)
    show_portfolios(portfolio_means, portfolio_risks)
    
    optimal_portfolio = optimize_portfolio(weights, returns)
    print_optimal_portfolio(optimal_portfolio, returns)
    show_optimal_portfolio(optimal_portfolio, returns, portfolio_means, portfolio_risks)