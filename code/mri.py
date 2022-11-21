import matplotlib.pyplot as plt
from fractals import fractal_dimension
from plot_utils import save_plot, create_image_gallery
import os


def calculate_mri_fractal_dimension(thresholds, images, markers):
    DIR = os.path.dirname(__file__)
    for threshold in thresholds:
        print(f"Próg = {threshold}")
        processed_images = []
        for imgname, marker in zip(images, markers):
            rel_path = f"dane/{imgname}_.png"
            df, processed_image = fractal_dimension(
                rel_path, threshold=threshold, min_depth=2, max_depth=11, label=imgname, marker=marker, return_image=True)
            processed_images.append(processed_image)
            print(f"Obraz {imgname}, df = {df:.2f}")

        background = create_image_gallery(processed_images)
        background.show()
        background.save(f"mri_prog_{threshold}.png")

        plt.legend()
        plt.title(f"Próg wykrywania = {threshold}")
        save_plot(plt, f"wykres_prog_{threshold}.png", axis=True)
        plt.show()
        print()


def main():
    calculate_mri_fractal_dimension(
        [150, 200, 250], ['a', 'b', 'c', 'd'], ['o', 'x', 'D', '^'])


if __name__ == '__main__':
    main()
