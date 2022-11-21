from posixpath import split
from PIL import Image, ImageDraw
import numpy as np
import matplotlib.pyplot as plt
import os

DIR = os.path.dirname(__file__)


def find_nearest_power_of_two(x):
    k = 0
    while True:
        if x // (2 ** k) == 0 or (x == (2 ** k)):
            break
        k += 1
    return 2 ** k


def fractal_dimension(imgname, q=0, threshold=220, min_depth=0, max_depth=10,
                      label=None, marker='o', return_image=False, debug=False, transformation=lambda x: x):
    with Image.open(os.path.join(DIR, imgname)) as img:
        if not img.mode == "RGB":
            img = img.convert("RGBA")
            background = Image.new(img.mode[:-1], img.size, (255, 255, 255))
            background.paste(img, img.split()[-1])
            img = background

        img = transformation(img)
        # img.show()
        width, height = img.size

        new_size = max(find_nearest_power_of_two(
            width), find_nearest_power_of_two(height))

        result = Image.new(img.mode, (new_size, new_size))
        result.paste(img, (0, 0))
        img = result.copy()

        data = np.asarray(result)
        data = np.sum(data, axis=2)

        # Replace matrix with 0s and 1s
        # data = np.where(data > threshold, 1, 0)
        data = np.where(data > threshold, data, 0)
        # Normalize
        data = data / np.sum(data)
        # Exponentiate
        # data = np.where(data == 0, data, np.float_power(data, q))

        eps_list = []
        I_list = []

        for m in range(0, int(np.log2(new_size)) + 1):
            k = 2 ** m
            if k < 2 ** min_depth:
                continue
            if k > 2 ** max_depth:
                break
            eps_list.append(1/k)

            img_copy = img.copy()
            draw = ImageDraw.Draw(img_copy)

            N = 0
            P_list = []
            L = new_size // k
            for i in range(0, k):
                for j in range(0, k):
                    matrix = data[i*L: (i+1)*L, j*L: (j+1)*L]
                    if (matrix_sum := np.sum(matrix)) > 0:
                        draw.rectangle(
                            (j*L, i*L, (j+1)*L, (i+1)*L), fill="red", outline='blue', width=1)
                        N += 1
                        P_list.append(matrix_sum)

            I_list.append(np.sum(np.float_power(P_list, q)))

            if debug:
                print(f"k = {k}: {N}")
                img_copy.show()

        eps_list = np.asarray(eps_list)
        I_list = np.asarray(I_list)

        # plt.plot(eps_list, I_list)
        # plt.show()

        logA = np.log(eps_list)
        logB = np.log(I_list)
        a, b = np.polyfit(logA, logB, 1)
        y_fit = np.exp(a*logA + b)

        plt.xscale('log')
        plt.yscale('log')
        plt.xlabel('$\log(\\varepsilon)$')
        plt.ylabel('$\log(I(\\varepsilon))$')
        plt.grid('on')
        plt.plot(eps_list, I_list, label=label, marker=marker, markevery=1)
        # plt.plot(I_list, marker=marker)
        # plt.plot(eps_list, y_fit, ':', color='r')

        if return_image:
            return -a / (1 - q), img_copy.crop((0, 0, width, height))
        return -a / (1 - q)


# jesli ponizej progu to 0
# jesli powyzej lub rowny to zostawiamy
# normalizujemy macierz (dzielimy kazdy element przez sume wszystkich elementow)

# liczac podmacierze, potegujemy kazdy element podmacierzy wykladnikiem q, dodajemy do siebie
# uzyskane wyniki, a na samym koncu mnozymy przez 1 / (q - 1)
# otrzymany wynik to P (stare N)

# input: NOISE
def calculate_D_s(data, s_min, s_max, q):
    data = np.cumsum(data)
    s_list = []
    D_list = []
    data_len = len(data)

    if s_max > data_len:
        s_max = data_len

    # s - dlugosc przedzialu
    for s_num in range(1, (data_len // s_min) + 1):
        splitted_data = np.array_split(data, s_num)
        D_temp_list = []
        for splitted_array in splitted_data:
            splitted_array = np.array(splitted_array)
            x = np.arange(0, len(splitted_array), 1)
            pa, pb, pc = np.polyfit(x, splitted_array, 2)
            splitted_array -= np.polyval([pa, pb, pc], x)

            D_temp_list.append(np.float_power(
                np.var(splitted_array), q / 2))
        D_list.append(np.float_power(np.mean(D_temp_list), 1/q))
        s_list.append(data_len / s_num)

        # print(f"s={s_list[-1]}, D={D_list[-1]}")

    s_list = np.asarray(s_list)
    D_list = np.asarray(D_list)
    logA = np.log(s_list)
    logB = np.log(D_list)

    a, b = np.polyfit(logA, logB, 1)
    y_fit = np.exp(a*logA + b)

    # plt.plot(s_list, D_list)
    # plt.plot(s_list, y_fit, ':', color='r')
    # plt.xscale('log')
    # plt.yscale('log')
    # plt.show()

    return a

print(fractal_dimension('miasta\\1.png', debug=True))