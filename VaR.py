import numpy as np 
import yfinance as yf 
import scipy   
import matplotlib.pyplot as plt
import pandas as pd 
import datetime as datetime

def download_data(stock, start_date, end_date):
    data = {} 
    ticker = yf.download(stock, start=start_date, end=end_date)
    data[stock] = ticker['Close']
    return pd.concat(data)

# n = 1 
def calculate_var(position, c, mu, sigma):
    v = scipy.stats.norm.ppf(1-c)
    var = position * (mu - sigma * v) 
    return var

# n > 1
def calculate_var_n(position, c, mu, sigma, n):
    v = scipy.stats.norm.ppf(1-c)
    var = position * (n * mu - np.sqrt(n) * sigma * v) 
    return var

if __name__ == "__main__":
    start = datetime.datetime(2014, 1, 1)
    end = datetime.datetime(2018, 1, 10)
    stock_data = download_data('C', start, end) # Citigroup ticker
    stock_data['returns'] = np.log(stock_data['C'] / stock_data['C'].shift(1))
    stock_data = stock_data[1:]
    
    S = 1000000 # Investment 
    c = 0.95 # Confidence level
    n = 10 # Number of days
    
    # We assume daily returns are normally distributed 
    mu = np.mean(stock_data['returns'])
    sigma = np.std(stock_data['returns'])
    
    print(f"Value at risk is: {calculate_var(S, c, mu, sigma):.2f}") # We can say with 95% confidence that we are not going to lose more than this amount
    print(f"Value at risk in {n} days is: {calculate_var_n(S, c, mu, sigma, n):.2f}") # We can say with 95% confidence that we are not going to lose more than this amount in n days