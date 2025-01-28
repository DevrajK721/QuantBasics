from scipy import stats 
from numpy import log, exp, sqrt 

def call_option_price(S, E, T, rf, sigma):
    # First we have to compute d1 and d2 
    d1 = (log(S / E) + (rf + sigma ** 2 / 2.0) * T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)
    print(f"The d1 and d2 parameters are {d1} and {d2}")
    
    # Use the N(X) distribution to calculate the price of the call option
    return S * stats.norm.cdf(d1) - E * exp(-rf * T) * stats.norm.cdf(d2)

def put_option_price(S, E, T, rf, sigma):
    # First we have to compute d1 and d2 
    d1 = (log(S / E) + (rf + sigma ** 2 / 2.0) * T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)
    print(f"The d1 and d2 parameters are {d1} and {d2}")
    
    # Use the N(X) distribution to calculate the price of the call option
    return -S * stats.norm.cdf(-d1) + E * exp(-rf * T) * stats.norm.cdf(-d2)
    
if __name__ == "__main__":
    # Underlying stock price at t = 0
    S0 = 100
    
    # Strike price
    E = 100 
    
    # Expiry time in years
    T = 1 
    
    # Risk-free rate
    rf = 0.05
    
    # Volatility of the underlying stock
    sigma = 0.2
    
    print(f"Call Option Price according to Black-Scholes model: {call_option_price(S0, E, T, rf, sigma):.2f}")
    print(f"Put Option Price according to Black-Scholes model: {put_option_price(S0, E, T, rf, sigma):.2f}")
     
    