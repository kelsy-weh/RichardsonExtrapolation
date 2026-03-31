import matplotlib.pyplot as plt
import numpy as np

def plot_cost_curve(Q, TC, Q_opt, title):
    plt.figure()
    plt.plot(Q, TC)
    plt.axvline(Q_opt, linestyle='--')
    plt.title(title)
    plt.xlabel("Order Quantity")
    plt.ylabel("Total Cost")
    plt.show()

def plot_error_bar(labels, error_h, error_h2, error_rich):
    x = np.arange(len(labels))

    plt.figure()
    plt.bar(x - 0.2, error_h, width=0.2, label="h")
    plt.bar(x, error_h2, width=0.2, label="h/2")
    plt.bar(x + 0.2, error_rich, width=0.2, label="Richardson")

    plt.xticks(x, labels)
    plt.legend()
    plt.title("Error Comparison")
    plt.show()