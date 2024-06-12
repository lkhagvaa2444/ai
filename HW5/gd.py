import math
import numpy as np
from numpy.linalg import norm

class Value:
    def __init__(self, data, _children=(), _op=''):
        self.data = data
        self._backward = lambda: None
        self.grad = None
        self.children = _children
        self.op = _op

    def backward(self, grad=None):
        if grad is None:
            grad = self.__class__(1.0)
        if self.grad is None:
            self.grad = grad
        else:
            self.grad += grad
        self._backward()
        for c in self.children:
            c.backward(self.grad * self.op)

def df(f, p, k, h=0.01):
    p1 = p.copy()
    p1[k] = Value(p[k].data + h)
    return (f(p1) - f(p)) / h

def grad(f, p, h=0.01):
    gp = p.copy()
    for k in range(len(p)):
        gp[k] = df(f, p, k, h)
    return gp

def gradientDescendent(f, p0, h=0.01, max_loops=100000, dump_period=1000):
    p = p0.copy()
    for i in range(max_loops):
        fp = f(p).data
        gp = grad(f, p, h)
        glen = norm(gp)
        if i % dump_period == 0: 
            print('{:05d}:f(p)={:.3f} p={:s} gp={:s} glen={:.5f}'.format(i, fp, str(p), str(gp), glen))
        if glen < 0.00001:
            break
        gh = np.multiply(gp, -1*h)
        p += gh
    print('{:05d}:f(p)={:.3f} p={:s} gp={:s} glen={:.5f}'.format(i, fp, str(p), str(gp), glen))
    return p
