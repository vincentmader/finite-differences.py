import matplotlib.pyplot as plt
import numpy as np

from finite_differences import METHODS

XMIN, XMAX, J = -5, 5, 100
DX = (XMAX-XMIN)/J


def plot_1(x, f):
    y = f(x)
    plt.plot(x, y, label="exponential")
    for (label, method) in METHODS:
        X, Y = method(x, y, DX)
        plt.plot(X, Y, label=label)
    plt.xlabel("$x$")
    plt.ylabel("$f(x)$")
    plt.legend(loc="upper left")
    plt.title("comparison of 1st order finite difference schemes")
    plt.show()


if __name__ == "__main__":
    f = np.exp
    x = np.linspace(XMIN, XMAX, J)

    plot_1(x, f)
