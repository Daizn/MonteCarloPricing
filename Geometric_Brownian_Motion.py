import numpy as np
s0 = 100 # initial stock price
mu = 0.08 # expected return
sigma = 0.15 # volatility
t = 1 # time 
steps = 252 # trading days
dt = t / steps # time increment
Z = np.random.normal(0,1, steps) # generate random numbers from standard normal distribution
St = s0 * np.exp((mu -0.5 * sigma ** 2) * dt + sigma * Z * dt ** 0.5) # final stock price