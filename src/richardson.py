def richardson_extrapolation(Q_h, Q_h2, p):
    return Q_h2 + (Q_h2 - Q_h) / (2**p - 1)