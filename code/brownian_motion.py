import matplotlib.pyplot as plt
from fbm import FBM
from fractals import fractal_dimension
from plot_utils import save_plot


def generate_brownian_motion(N, H, dpi=None):
    f = FBM(N, H)
    x = f.times()
    y = f.fbm()

    plt.plot(x, y)
    if dpi != None:
        save_plot(plt, dpi=dpi)
    else:
        save_plot(plt)
    plt.show()


def calculate_brownian_dimension():
    N = int(10e4)
    H_list = [0.5]
    for H in H_list:
        generate_brownian_motion(N, H, dpi=600)
        df = fractal_dimension("plot.png", max_depth=11)

        print(f"Wyliczono: H = {H}, df = {df}")
        print(f"Teoretycznie: H = {H}, df = {2 - H}")
        print()


def main():
    calculate_brownian_dimension()


if __name__ == '__main__':
    main()
