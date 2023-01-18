import os

import matplotlib.pyplot as plt
import numpy as np

from finite_differences import METHODS

XMIN, XMAX, NX = -0, 10, 100
DX = (XMAX-XMIN) / NX

HMIN, HMAX, NH = 1e-15, 1e0, 100
X0 = 0

MPL_THEME = "./mpl-styles/dark.mplstyle"
plt.style.use(MPL_THEME)


def plot_1(x, f):
    y = f(x)
    plt.plot(x, y, label="exponential")
    for (label, method) in METHODS:
        Y = method(x, f, DX)
        plt.plot(x, Y, label=label)
    plt.xlabel("$x$")
    plt.ylabel("$f(x)$")
    plt.legend(loc="upper left")
    plt.title("comparison of 1st order finite difference schemes")
    path = os.path.join("..", "out", "fd-comparison.png")
    plt.savefig(path)
    plt.show()


def plot_2(x, f):
    y = f(x)
    plt.plot(x, y - y, label="exponential")
    for (label, method) in METHODS:
        Y = method(x, f, DX)
        err = Y - f(x)
        plt.plot(x, err, label=label)
    plt.xlabel("$x$")
    plt.ylabel("error $f_{num}(x) - f(x)$")
    plt.legend(loc="upper left")
    plt.title("comparison of 1st order finite difference scheme error")
    path = os.path.join("..", "out", "fd-error-vs-x.png")
    plt.savefig(path)
    plt.show()


def plot_3(f):
    h_range = np.logspace(-15, 0, 100)
    for (label, method) in METHODS:
        Y = method([X0], f, h_range)
        err = Y / f(X0)
        plt.plot(x, err, label=label)

    plt.xlabel("$\Delta x$")
    plt.ylabel("error $f_{num}(x) / f(x)$")
    plt.legend(loc="upper left")
    plt.title("comparison of 1st order finite difference scheme error")
    path = os.path.join("..", "out", "fd-error-vs-h.png")
    plt.savefig(path)
    plt.show()


if __name__ == "__main__":
    f = np.exp
    x = np.linspace(XMIN, XMAX, NX)

    plot_1(x, f)
    plot_2(x, f)
    plot_3(f)
