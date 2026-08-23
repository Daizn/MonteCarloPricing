import numpy as np
s0 = 100 # initial stock price
mu = 0.08 # expected return
sigma = 0.15 # volatility
t = 1 # time 
steps = 252 # trading days
dt = t / steps # time increment
Z = np.random.normal(0,1, steps) # generate random numbers from standard normal distribution
current_price = s0
price_list = []
for i in Z:
    current_price = current_price * np.exp((mu -0.5 * sigma ** 2) * dt + sigma * i * np.sqrt(dt)) # final stock price
    price_list.append(current_price)
print(price_list)
