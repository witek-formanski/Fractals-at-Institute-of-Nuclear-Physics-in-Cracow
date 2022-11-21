from plot_utils import calculate_q_plot
from stock_exchange import calculate_stock_fractal_dimension
from PIL import ImageOps
import re

# with open("qlist.txt", "r") as file:
#     for line in file:
#         stripped_line = line.strip()
#         x = re.search("df = ([-\d.]+)", stripped_line)
#         print(x.group(1))


def main():
    # calculate_q_plot([0, 0.3, 0.6, 0.9, 1.2, 1.5, 1.8, 2.1], 'images/fractals/triangle.jpg',
    #                  0, transformation=lambda x: ImageOps.invert(ImageOps.grayscale(x).convert("RGB")))
    calculate_q_plot([0, 2], 'plot.png',
                     0, transformation=lambda x: ImageOps.invert(ImageOps.grayscale(x).convert("RGB")))


if __name__ == '__main__':
    main()
