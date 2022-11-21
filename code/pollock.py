import matplotlib.pyplot as plt
from fractals import fractal_dimension
from plot_utils import save_plot, create_image_gallery, calculate_q_plot
from PIL import ImageOps
import numpy as np


def calculate_pollock_fractal_dimension(threshold, q):
    images = []
    df_list = []
    for i in range(0, 9):
        df, img = fractal_dimension(f'images/pollock/{i}.jpg', q=q, threshold=threshold, min_depth=5, max_depth=11,
                                    label=i, return_image=True, debug=False,
                                    transformation=lambda x: ImageOps.grayscale(x).convert("RGB"))
        print(f"Obraz {i}, df = {df:.4f}")
        images.append(img)
        df_list.append(df)

    background = create_image_gallery(images)
    background.show()
    background.save(f"pollock_prog_{threshold}_q_{q}.png")

    plt.legend()
    plt.title(f"Próg wykrywania = {threshold}")
    save_plot(plt, f"wykres_pollock_prog_{threshold}_q_{q}.png", axis=True)
    plt.show()

    y = np.array(df_list)
    x = np.array([t for t in range(len(y))])
    plt.plot(y, marker='o')
    ax = plt.gca()
    ax.set_xticklabels(
        [0, 1935, 1937, 1941, 1943, 1946, 1948, 1952, 1955, 1955])
    a, b = np.polyfit(x, y, 1)
    y_fit = a*x + b
    plt.xlabel("Rok powstania obrazu")
    plt.ylabel(f"$D_{q}$")
    plt.title("Ewolucja fraktalna twórczości Pollocka w czasie", fontsize=16)
    plt.plot(x, y_fit, ':', color='r')
    plt.grid('on')
    save_plot(plt, f"ewolucja_pollock_prog_{threshold}_q_{q}.png", axis=True)
    plt.show()


def main():
    calculate_pollock_fractal_dimension(threshold=350, q=4)
    # calculate_q_plot(350)


if __name__ == '__main__':
    main()
