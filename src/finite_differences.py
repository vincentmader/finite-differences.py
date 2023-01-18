def first_order_forward(x, f, h):
    return (f(x+h) - f(x)) / h


def first_order_backward(x, f, h):
    return (f(x) - f(x-h)) / h


def first_order_central(x, f, h):
    return (f(x+h) - f(x-h)) / (2*h)


METHODS = [
    ("1st order forward", first_order_forward),
    ("1st order backward", first_order_backward),
    ("1st order central", first_order_central)
]
