import numpy as np 
import pandas as pd  
import matplotlib.pyplot as plt 

NUM_OF_SIMULATIONS = 1000

def stock_monte_carlo(S0, mu, sigma, N=1000):
    result = []
    for _ in range(NUM_OF_SIMULATIONS):
        prices =[S0]
        for _ in range(N):
            # We simulate the change day by day (t = 1) 
            stock_price = prices[-1] * np.exp((mu - 0.5 * sigma ** 2) +
                                                sigma * np.random.normal())
            prices.append(stock_price)
        result.append(prices)
        
    simulation_data = pd.DataFrame(result)
    simulation_data = simulation_data.T # Transpose the data so the columns are the simulations
    simulation_data['mean'] = simulation_data.mean(axis=1)
    print(simulation_data)
    plt.style.use('default')
    fig, ax = plt.subplots()
    fig.patch.set_facecolor('#1e1e2e')
    ax.set_facecolor('white')
    ax.plot(simulation_data[:-2], alpha=0.7)
    ax.set_title('Monte Carlo Simulation for Stock Prices', color='white')
    ax.set_xlabel('Day', color='white')
    ax.set_ylabel('Stock Price', color='white')
    ax.grid(False)
    plt.show()
    
    print('Prediction for future stock price: ' + str(simulation_data.iloc[-1]['mean']))
    

if __name__ == "__main__":
    stock_monte_carlo(50, 0.0002, 0.01)