# Regression Linear
# Y = MX + B

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Reading Data
data = pd.read_csv('headbrain.csv')
print(data.shape)
data.head()

# Collecting X and Y
X = data['Head Size (cm^3)'].values
Y = data['Brain Weight (grams)'].values

# Mean X and Y
mean_x = np.mean(X)
mean_y = np.mean(Y)

# Total Number of values
m = len(X)

# Using the formula to calculate b1 and b2
numer = 0
denom = 0
for i in range(m):
    numer += (X[i] - mean_x) * (Y[i] - mean_y)
    denom += (X[i] - mean_x) ** 2
b1 = numer/denom
b0 = mean_y - (b1 * mean_x)

# print coefficients
print(b1,b0)

# Plotting values and regression Line
max_x = np.max(X) + 100
min_x = np.max(X) - 100

# Calculating line values x and y
x = np.linspace(min_x,max_x,1000)
y = b0 + b1 * x

# plotting line
plt.plot(x,y,color='red',label='Regression Line')

# ploting Scatter Points
plt.scatter(X,Y,c='blue',label='Scatter Plot')

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
#plt.show()

ss_t = 0
ss_r = 0
for i in range(m):
    y_pred = b0 + b1 * X[i]
    ss_t += (Y[i] - mean_y) ** 2
    ss_r += (Y[i] - y_pred) ** 2
r2 = 1 - (ss_r/ss_t)
print(r2)