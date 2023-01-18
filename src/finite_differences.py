import numpy as np


def first_order_forward(x, y, h):
    ydot = []
    for i, _ in enumerate(x):
        if i+1 >= len(y):
            continue
        y_i = (y[i+1] - y[i]) / h
        ydot = np.append(ydot, y_i)
    return x[:-1], ydot


def first_order_backward(x, y, h):
    ydot = []
    for i, _ in enumerate(x):
        if i-1 < 0:
            continue
        y_i = (y[i] - y[i-1]) / h
        ydot = np.append(ydot, y_i)
    return x[1:], ydot


def first_order_central(x, y, h):
    ydot = []
    for i, _ in enumerate(x):
        if i-1 < 0 or i+1 >= len(y):
            continue
        y_i = (y[i+1] - y[i-1]) / (2*h)
        ydot = np.append(ydot, y_i)
    return x[1:-1], ydot


METHODS = [
    ("1st order forward", first_order_forward),
    ("1st order backward", first_order_backward),
    ("1st order central", first_order_central)
]
