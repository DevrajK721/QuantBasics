import numpy as np 
import yfinance as yf
import datetime as datetime
import pandas as pd 

def download_data(stock, start_date, end_date):
    data = {} 
    ticker = yf.download(stock, start=start_date, end=end_date)
    data[stock] = ticker['Close']
    return pd.concat(data)

class ValueatRiskMonteCarlo():
    def __init__(self, S, mu, sigma, c, n, iterations):
        self.S = S
        self.mu = mu
        self.sigma = sigma
        self.c = c
        self.n = n  
        self.iterations = iterations
        
    def simulation(self):
        rand = np.random.normal(0, 1, [1, self.iterations])
        stock_price = self.S * np.exp(self.n*(self.mu - 0.5*self.sigma**2) + self.sigma*np.sqrt(self.n)*rand)
        stock_price = np.sort(stock_price)
        percentile = np.percentile(stock_price, (1 - self.c) * 100)
        
        return self.S - percentile 
    
if __name__ == "__main__":
    S = 1e6 # Investment
    c = 0.95 # Confidence level
    n = 1 # Number of days
    iterations = 1000000
    start = datetime.datetime(2014, 1, 1)
    end = datetime.datetime(2017, 1, 10)
    citi = download_data('C', start, end)
    citi['returns'] = np.log(citi['C'] / citi['C'].shift(1))
    mu = np.mean(citi['returns'])
    sigma = np.std(citi['returns'])
    
    model = ValueatRiskMonteCarlo(S, mu, sigma, c, n, iterations)
    print(f"Value at Risk with Monte Carlo Simulation: {model.simulation():.2f}")