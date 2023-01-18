import matplotlib.pyplot as plt
import numpy as np

from finite_differences import METHODS

XMIN, XMAX, J = -5, 5, 100
DX = (XMAX-XMIN)/J

MPL_THEME = "./mpl-styles/dark.mplstyle"
plt.style.use(MPL_THEME)


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


def plot_2(x, f):
    y = f(x)
    for (label, method) in METHODS:
        X, Y = method(x, y, DX)
        err = Y - f(X)
        plt.plot(X, err, label=label)
    plt.xlabel("$x$")
    plt.ylabel("error $f_{num}(x) - f(x)$")
    plt.legend(loc="upper left")
    plt.title("comparison of 1st order finite difference scheme error")
    plt.show()


if __name__ == "__main__":
    f = np.exp
    x = np.linspace(XMIN, XMAX, J)

    plot_1(x, f)
    plot_2(x, f)
