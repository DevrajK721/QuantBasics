import matplotlib.pyplot as plt
import numpy as np 

def vasicek_model(r0, kappa, theta, sigma, T = 1, N = 1000):
    dt = T / float(N)
    t = np.linspace(0, T, N + 1)
    
    rates = [r0]
         
    for _ in range(N):
        dr = kappa * (theta - rates[-1]) * dt + sigma * np.sqrt(dt) * np.random.normal(0, 1)
        rates.append(rates[-1] + dr)
        
    return t, rates

def plot_vasicek(t, rates):
    plt.plot(t, rates)
    plt.xlabel('Time (t)')
    plt.ylabel('Rates (r(t))')
    plt.title('Vasicek Model')
    plt.show()
    
if __name__ == "__main__":
    r0 = 1.3
    kappa = 0.9
    theta = 1.5
    sigma = 0.01
    T = 1
    N = 1000
    
    t, rates = vasicek_model(r0, kappa, theta, sigma, T, N)
    plot_vasicek(t, rates)