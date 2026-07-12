import numpy as np
import pandas as pd
import scipy
import matplotlib.pyplot as plt

print("NumPy:", np.__version__)
print("Pandas:", pd.__version__)
print("SciPy:", scipy.__version__)

prices = np.random.normal(0, 1, 10000)

plt.hist(prices, bins=50)
plt.show()