# Micrograd Gradient Descent

This Python module implements gradient descent optimization using micrograd.

## Usage

### Example 1: Single Variable Function Optimization

```python
import gd

def f(p):
    return (p[0]-1)**2+(p[1]-2)**2+(p[2]-3)**2

p = [0.0, 0.0, 0.0]
gd.gradientDescendent(f, p)
Example 2: Regression
python
Copy code
import matplotlib.pyplot as plt
import numpy as np
import gd

x = np.array([0, 1, 2, 3, 4], dtype=np.float32)
y = np.array([1.9, 3.1, 3.9, 5.0, 6.2], dtype=np.float32)

def predict(a, xt):
    return a[0]+a[1]*xt

def MSE(a, x, y):
    total = 0
    for i in range(len(x)):
        total += (y[i]-predict(a,x[i]))**2
    return total

def loss(p):
    return MSE(p, x, y)

p = [0.0, 0.0]
plearn = gd.gradientDescendent(loss, p, max_loops=3000, dump_period=1)
Test Cases
To run the test cases, use the provided scripts:

gdArray.py
python
Copy code
import gd

def f(p):
    return (p[0]-1)**2+(p[1]-2)**2+(p[2]-3)**2

p = [0.0, 0.0, 0.0]
gd.gradientDescendent(f, p)
gdRegression.py
python
Copy code
import matplotlib.pyplot as plt
import numpy as np
import gd

x = np.array([0, 1, 2, 3, 4], dtype=np.float32)
y = np.array([1.9, 3.1, 3.9, 5.0, 6.2], dtype=np.float32)

def predict(a, xt):
    return a[0]+a[1]*xt

def MSE(a, x, y):
    total = 0
    for i in range(len(x)):
        total += (y[i]-predict(a,x[i]))**2
    return total

def loss(p):
    return MSE(p, x, y)

p = [0.0, 0.0]
plearn = gd.gradientDescendent(loss, p, max_loops=3000, dump_period=1)