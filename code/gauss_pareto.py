import numpy as np
import matplotlib.pyplot as plt


def normalize(x):
    # x_wi = (x_i - mu) / sigma
    std = np.std(x)
    mean = np.mean(x)
    return (x - mean) / std


def plot_gauss_vs_pareto():
    N = 1000000
    BINS = 500
    K = 20

    # Gauss
    x1 = np.random.normal(0, 1, N)

    # Pareto (negative values and normalization)
    x2 = np.multiply(np.random.pareto(1.5, N), np.sign(x1))
    x2 = normalize(x2)

    plt.subplot(2, 2, 1)
    plt.plot(x1)
    plt.title("Gauss")

    plt.subplot(2, 2, 2)
    plt.plot(x2)
    plt.title("Pareto")

    plt.subplot(2, 2, 3)
    for data, label in zip([x1, x2], ["Gauss", "Pareto"]):
        plt.hist(data, BINS, [-K, K], label=label)
    plt.title("Histogram")
    plt.legend()

    plt.subplot(2, 2, 4)
    for data, label in zip([x1, x2], ["Gauss", "Pareto"]):
        plt.hist(data, BINS, [-K, K], label=label)
        plt.xscale('log')
        plt.yscale('log')
    plt.title("Histogram (log-log)")
    plt.legend()

    print(f"Min: {np.min(x2)}")
    print(f"Max: {np.max(x2)}")

    plt.show()


def main():
    plot_gauss_vs_pareto()


if __name__ == '__main__':
    main()
