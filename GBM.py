import matplotlib.pyplot as plt
import numpy as np 


def simulate_geometric_random_walk(S_0, T = 2, N = 1000, mu = 0.1, sigma = 0.05):
    dt = T / N 
    t = np.linspace(0, T, N) 
    # Standard normla distribution N(0, 1), to achieve N(0, dt), we use sqrt(dt) * N(0, 1)
    W = np.random.standard_normal(size = N) 
    W = np.cumsum(W) * np.sqrt(dt)
    X = (mu - 0.5 * sigma ** 2) * t + sigma * W
    S = S_0 * np.exp(X)
    
    return t, S

def plot_simulation(t, S):
    plt.figure(facecolor = '#1e1e2e')
    ax = plt.gca()
    ax.set_facecolor('#1e1e2e')
    ax.plot(t, S, color = '#ff073a')
    ax.set_xlabel('Time', color = 'white')
    ax.set_ylabel('Stock price', color = 'white')
    ax.set_title('Geometric random walk', color = 'white')
    ax.tick_params(axis = 'x', colors = 'white')
    ax.tick_params(axis = 'y', colors = 'white')
    plt.show()
    
if __name__ == '__main__':
    time, data = simulate_geometric_random_walk(10)
    plot_simulation(time, data)