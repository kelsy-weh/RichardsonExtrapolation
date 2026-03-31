import numpy as np
import pandas as pd

from src.cost_function import total_cost
from src.eoq_calculation import exact_eoq, approximate_eoq
from src.richardson import richardson_extrapolation
from src.error_analysis import compute_error
from src.plotting import plot_cost_curve, plot_error_bar

products = {
    "Noodles": {"D": 7200, "S": 50, "H": 2},
    "Soft Drinks": {"D": 5000, "S": 80, "H": 3},
    "Canned Goods": {"D": 3000, "S": 60, "H": 2.5}
}

Q_min = 10
Q_max = 1000
h = 50
h2 = 25
p = 2

results = []

for name, params in products.items():
    D, S, H = params["D"], params["S"], params["H"]

    Q_exact = exact_eoq(D, S, H)

    Q_values_h = np.arange(Q_min, Q_max, h)
    TC_h = total_cost(Q_values_h, D, S, H)
    Q_h = approximate_eoq(Q_values_h, TC_h)

    Q_values_h2 = np.arange(Q_min, Q_max, h2)
    TC_h2 = total_cost(Q_values_h2, D, S, H)
    Q_h2 = approximate_eoq(Q_values_h2, TC_h2)

    Q_rich = richardson_extrapolation(Q_h, Q_h2, p)

    error_h = compute_error(Q_exact, Q_h)
    error_h2 = compute_error(Q_exact, Q_h2)
    error_rich = compute_error(Q_exact, Q_rich)

    results.append([name, Q_exact, Q_h, Q_h2, Q_rich, error_h, error_h2, error_rich])

df = pd.DataFrame(results, columns=[
    "Product", "EOQ", "Q_h", "Q_h2", "Q_rich",
    "Error_h", "Error_h2", "Error_rich"
])

print(df)

plot_error_bar(df["Product"], df["Error_h"], df["Error_h2"], df["Error_rich"])