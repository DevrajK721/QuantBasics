import numpy.random as nrp 
import numpy as np
import matplotlib.pyplot as plt

# Function to generate a brownian motion
def wiener_process(dt = 0.1, x0 = 0, n = 1000):
    """
    Args:
        dt (float, optional): _description_. Defaults to 0.1.
        x0 (int, optional): _description_. Defaults to 0.
        n (int, optional): _description_. Defaults to 1000.
    """
    # Initially, W(t = 0) = 0, so we initialize W(t) with zeroes. 
    W = np.zeros(n + 1)
    
    # We now create n+1 time steps 
    t = np.linspace(0, n, n + 1)
    
    # Now, we have to calculate the Wiener process. 
    # We have to use the cumulative sum:
        # On every step the additional value is drawn from a normal distribution with mean 0 and variance dt
            # N(0, dt)
            # N(0, dt) = sqrt(dt) * N(0, 1)
    W[1 : n + 1] = np.cumsum(nrp.normal(0, np.sqrt(dt), n)) 
    
    return t, W

def plot_process(t, W):
    plt.figure(facecolor='#1e1e2e')
    ax = plt.gca()
    ax.set_facecolor('#1e1e2e')
    ax.plot(t, W, color='#ff073a')  # Neon red color for the line
    ax.set_xlabel('Time', color='white')
    ax.set_ylabel('Wiener process', color='white')
    ax.set_title('Wiener process', color='white')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    plt.show()

if __name__ == '__main__':
    t, W = wiener_process()
    plot_process(t, W)
