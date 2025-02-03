import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 

NUM_OF_SIMULATIONS = 1000 # Number of interest rate processes 
NUM_OF_POINTS = 200 # Number of points in time

def monte_carlo_simulation(x, r0, kappa, theta, sigma, T = 1):
    dt  = T / float(NUM_OF_POINTS)
    result = []
    
    for _ in range(NUM_OF_SIMULATIONS):
        rates = [r0] 
        for _ in range(NUM_OF_POINTS):
             dr = kappa * (theta - rates[-1]) * dt + sigma * np.sqrt(dt) * np.random.normal(0, 1)
             rates.append(rates[-1] + dr)
             
        result.append(rates)
    
    simulation_data = pd.DataFrame(result)
    simulation_data = simulation_data.T
    
    integral_sum = simulation_data.sum() * dt 
    present_integral_sum = np.exp(-integral_sum)
    bond_price = x * np.mean(present_integral_sum)
    print(f"Bond Price based on Monte Carlo Simulation: {bond_price:.2f}")
    
    return simulation_data

def plot_interest_rate(simulation_data):
    plt.plot(simulation_data)
    plt.xlabel('Time (t)')
    plt.ylabel('Rates (r(t))')
    plt.title('Vasicek Model')
    plt.show()
    
if __name__ == "__main__":
    simulation_data = monte_carlo_simulation(1000, 0.5, 0.3, 0.9, 0.03)
    plot_interest_rate(simulation_data)
