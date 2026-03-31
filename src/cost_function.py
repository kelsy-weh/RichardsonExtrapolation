import numpy as np

def total_cost(Q, D, S, H):
    return (D * S / Q) + (H * Q / 2)