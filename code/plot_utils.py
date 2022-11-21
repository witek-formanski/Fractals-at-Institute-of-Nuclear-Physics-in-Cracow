import numpy as np
from PIL import Image, ImageOps
from fractals import fractal_dimension
import matplotlib.pyplot as plt


def save_plot(plt, name="plot.png", axis=False, dpi=500):
    if not axis:
        plt.axis('off')

    fig = plt.gcf()
    fig.savefig(name, dpi=dpi)


def create_image_gallery(images):
    width_list = [image.size[0]
                  for image in images]
    background = Image.new("RGB",
                           (np.sum(width_list),
                            max([image.size[1]
                                 for image in images])
                            ),
                           (255, 255, 255)
                           )

    for i in range(len(images)):
        current_image = images[i]
        width, height = current_image.size
        left = int(np.sum(width_list[0:i]))
        background.paste(
            current_image, (left, 0, left + width, height))

    return background


def calculate_q_plot(q_list, image, threshold, transformation=lambda x: x):
    images = []
    df_list = []
    for q in q_list:
        df, img = fractal_dimension(imgname=image, q=q, threshold=threshold, label=f"q = {q}", min_depth=0, max_depth=11,
                                    return_image=True, debug=False,
                                    transformation=transformation)
        print(f"q = {q}, df = {df:.4f}")
        images.append(img)
        df_list.append(df)

    plt.legend()
    plt.show()

    background = create_image_gallery(images)
    background.show()

    plt.plot(q_list, df_list, marker='o')
    plt.show()
