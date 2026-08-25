import numpy as np
import matplotlib.pyplot as plt
s0 = 100 #initial stock price
repeat = 1000 # number of simulations
simulation = np.full(repeat, s0) #full array of initial stock price
mu = 0.08 # expected return
sigma = 0.15 # volatility
t = 1 # time 

steps = 252 # trading days

current_price = simulation
price_list = []


dt = t / steps # time increment
Z = np.random.normal(0,1, (repeat, steps)) # generate random numbers from standard normal distribution

for i in range(steps):
    current_price = current_price * np.exp((mu -0.5 * sigma ** 2) * dt + sigma * Z[:, i] * np.sqrt(dt)) # final stock price
    price_list.append(current_price.copy())

price_array = np.array(price_list) # convert list to array
print(price_array.shape) # shape of the array
random_simulation = np.random.choice(repeat, 10, replace=False) # select 10 random simulations
for i in random_simulation:
    plt.plot(price_array[:, i])

plt.xlabel("Trading day")
plt.ylabel("Stock price")
plt.title("GBM Simulated Stock Prices")
plt.show()