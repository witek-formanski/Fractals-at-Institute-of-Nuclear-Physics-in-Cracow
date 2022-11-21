import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from fractals import fractal_dimension, calculate_D_s
from plot_utils import save_plot


def calculate_stock_fractal_dimension(dpi=None):
    data = yf.download('EURPLN=X')
    data = data.iloc[230:, :]
    prices = np.array(data["Close"])
    plt.plot(prices)
    if dpi != None:
        save_plot(plt, dpi=dpi)
    else:
        save_plot(plt)
    plt.show()

    df = fractal_dimension("plot.png", max_depth=11)
    print(f"df = {df}")


def main():
    # calculate_stock_fractal_dimension(600)
    data = yf.download('EURPLN=X')
    data = data.iloc[230:, :]
    prices = np.array(data["Close"])
    # MOTION -> NOISE
    prices = np.diff(np.log(prices))

    eps = 1e-10
    q_list = np.arange(-1, 1.2, 0.2)
    q_list = q_list[np.abs(q_list - 0) > eps]
    h_list = []
    for q in q_list:
        h = calculate_D_s(prices, 10, 10000, q)
        h_list.append(h)

    plt.plot(q_list, h_list)
    plt.show()


if __name__ == '__main__':
    main()
