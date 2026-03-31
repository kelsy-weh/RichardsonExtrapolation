import numpy as np

def exact_eoq(D, S, H):
    return np.sqrt((2 * D * S) / H)

def approximate_eoq(Q_values, cost_values):
    return Q_values[cost_values.argmin()]