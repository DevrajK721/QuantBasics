from math import exp 

def future_discrete_value(x, r, n):
    return x * (1 + r) ** n

def present_discrete_value(x, r, n):
    return x * (1 + r) ** (-n)

def future_continuous_value(x, r, t):
    return x * exp(r * t) 

def present_continuous_value(x, r, t):
    return x * exp(-r * t) 

if __name__ == "__main__":
    x = 100 # Value of the investment
    r = 0.05 # Interest rate
    n = 5 # Duration (Years) - Discrete
    t = 5 # Duration (Years) - Continuous
    
    # Discrete 
    print(f"Future Value of x: {future_discrete_value(x, r, n)}")
    print(f"Present Value of x: {present_discrete_value(x, r, n)}")
    
    # Continuous
    print(f"Future Value of x: {future_continuous_value(x, r, t)}")
    print(f"Present Value of x: {present_continuous_value(x, r, t)}")
        